#!/usr/bin/env python3
from typing import Any, Sequence, Union
"""
Module for task 10"""


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Type annotated function to return the first element of a list or None"""
    if lst:
        return lst[0]
    else:
        return None
