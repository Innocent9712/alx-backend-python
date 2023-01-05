#!/usr/bin/env python3
from typing import Callable
"""
Module for task 8"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Type annotated function that takes a float multiplier as argument and
    returns a function that multiplies a float by multiplier"""
    return lambda x: x * multiplier
