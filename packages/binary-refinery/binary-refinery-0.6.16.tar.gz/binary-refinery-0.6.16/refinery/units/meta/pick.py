#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Iterable, List
from refinery.units import Arg, Unit, Chunk
from refinery.lib.tools import begin

from collections import deque


class pick(Unit):
    """
    Picks sequences from the array of multiple inputs. For example, `pick 0 2:`
    will return all but the second ingested input (which has index `1`).
    """
    def __init__(self, *slice: Arg.Bounds(nargs='*', default=[slice(None, None)])):
        super().__init__(slice=slice)

    def filter(self, chunks: Iterable[Chunk]):
        chunks = begin(chunks)
        if chunks is None:
            return
        slices = deque(self.args.slice)
        discards = 0
        consumed = False
        remaining: List[Chunk] = []

        def discardable(s: slice):
            return s.stop and s.stop >= 0 and (s.step or 1) > 0 \
                and all(t.start >= s.stop for t in slices)

        while slices:
            s: slice = slices.popleft()

            if not consumed:
                if not discardable(s):
                    self.log_debug(F'consumed input into buffer after {discards} skips')
                    for chunk in chunks:
                        if not chunk.visible:
                            yield chunk
                            continue
                        remaining.append(chunk)
                    consumed = True

            start = s.start
            stop = s.stop
            if start is not None:
                start -= discards
            if stop is not None:
                stop -= discards
            if consumed:
                yield from remaining[slice(start, stop, s.step)]
                continue
            while start:
                try:
                    chunk = next(chunks)
                except StopIteration:
                    stop = None
                    break
                if chunk.visible:
                    start -= 1
                    stop -= 1
                    discards += 1
                else:
                    yield chunk
            if stop is None:
                yield from chunks
                continue
            while stop:
                try:
                    chunk = next(chunks)
                except StopIteration:
                    break
                if chunk.visible:
                    stop -= 1
                    discards += 1
                yield chunk
