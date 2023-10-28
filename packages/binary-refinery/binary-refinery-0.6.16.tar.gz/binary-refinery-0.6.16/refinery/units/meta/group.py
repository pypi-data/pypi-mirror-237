#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Iterable, List
from refinery.units import Arg, Unit, Chunk


class group(Unit):
    """
    Group incoming chunks into frames of the given size.
    """
    def __init__(self, size: Arg.Number(help='Size of each group; must be at least 2.', bound=(2, None))):
        super().__init__(size=size)

    def process(self, data: Chunk):
        members: List[Chunk] = data.temp or []
        if len(members) >= self.args.size:
            raise RuntimeError(F'received {len(members) + 1} items in group')
        yield data
        yield from members

    def filter(self, chunks: Iterable[Chunk]):
        members = []
        header = None
        for chunk in chunks:
            if not chunk.visible:
                yield chunk
                continue
            if len(members) > self.args.size - 2:
                yield header
                header = None
            if header is None:
                chunk.temp = members
                header = chunk
                members.clear()
            else:
                members.append(chunk)
        if header is not None:
            yield header
