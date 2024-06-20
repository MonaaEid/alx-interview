#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    if x == 0 or x == 1:
        return None
    if x == 2:
        return "Ben"
    if x == 3:
        return "Maria"

    return "Maria" if sum([1 for n in nums if n % 2 == 0]) == 0 else "Ben"
