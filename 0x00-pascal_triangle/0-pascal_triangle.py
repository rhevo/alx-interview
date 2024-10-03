#!/usr/bin/python3
"""
0. Pascal's Triangle
"""

from typing import List

def pascal_triangle(n: int) -> List[List[int]]:
    """
    Generate Pascal's triangle of n levels.

    Args:
        n (int): Number of levels to generate

    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle.
    """
    res = []
    if n > 0:
        for i in range(1, n + 1):
            level = []
            C = 1
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j
            res.append(level)
    return res
