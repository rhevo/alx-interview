#!/usr/bin/python3
"""
Pascal's Triangle
"""

def pascal_triangle(n):
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
            C = 1  # Initialize the first value in the row
            for j in range(1, i + 1):
                level.append(C)
                C = C * (i - j) // j  # Update C to the next binomial coefficient
            res.append(level)
    return res


# Example Usage
if __name__ == "__main__":
    n = 5
    triangle = pascal_triangle(n)
    for row in triangle:
        print(row)
