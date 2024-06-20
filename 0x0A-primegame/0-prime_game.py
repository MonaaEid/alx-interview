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
    if x == 2:
        return "Ben"
    if x == 3:
        return "Maria"
    primes = prime(max(nums))
    score = 0
    for i in range(x):
        score += sum([1 for j in primes if j <= nums[i]])
    if score % 2 == 0:
        return "Maria"
    return "Ben"

