#!/usr/bin/python3
"""Prime Game"""


def prime(n):
    """return list of prime numbers"""
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def isWinner(x, nums):
    """Prime Game"""
    if x == 0 or x == 1:
        return None
    n = max(nums)
    primes = prime(n)
    score = {1: 0, 2: 0}
    for i in range(1, x + 1):
        for j in nums:
            if j in primes:
                score[i % 2] += 1
    if score[1] == score[2]:
        return None
    if score[1] > score[2]:
        return "Maria"
    return "Ben"
