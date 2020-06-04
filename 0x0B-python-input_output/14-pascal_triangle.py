#!/usr/bin/python3
"""
This file defines a function
that creates a pascal's triangle
"""


def pascal_triangle(n):
    """
    Function defining the logic to
    create pascal's triangle
    """
    if (n <= 0):
        return ([])
    if n == 1:
        return [[1]]
    pascal_triangle = []
    for i in range(0, n):
        pascal_triangle.append([1])
    for key, value in enumerate(pascal_triangle):
        for m in range(0, key):
            value.append(int(result(key, m + 1)))
    return pascal_triangle


def factorial(x):
    """
    Function that returns factorial
    """
    if x == 0:
        return 1
    fact = 1
    for i in range(1, x + 1):
        fact = fact * i
    return fact


def result(n, k):
    """
    Function that returns result
    """
    return (factorial(n) / (factorial(k) * factorial(n - k)))
