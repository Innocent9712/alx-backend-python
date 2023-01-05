#!/usr/bin/env python3
from typing import List, Tuple, Iterable, Sequence
"""
Module for task 9"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Type annotated function to return a list of tuples of the input list"""
    return [(i, len(i)) for i in lst]
