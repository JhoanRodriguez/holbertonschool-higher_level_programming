#!/usr/bin/python3
"""Finds peak in unsorted list of integers"""


def find_peak(list_of_integers):
    """Finds peak in unsorted list of integers"""
    if not list_of_integers:
        return None
    return max(list_of_integers)
