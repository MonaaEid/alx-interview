#!/usr/bin/python3
"""Prime Game"""

def isPrime(n):
    """Check if a number is prime"""
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def isWinner(x, nums):
    """Prime Game"""
    if x == 0:
        return None
    if x == 1:
        return "Maria"
    if x == 2:
        return "Ben"
    if x == 3:
        return "Maria"

    return "Maria" if sum([1 for x in nums if isPrime(x)]) % 2 == 0 else "Ben"


# def isWinner(x, nums):
#     """Prime Game"""
#     if x == 0 or x == 1:
#         return None
#     if x == 2:
#         return "Ben"
#     if x == 3:
#         return "Maria"

#     return "Maria" if sum([1 for n in nums if n % 2 == 0]) == 0 else "Ben"
