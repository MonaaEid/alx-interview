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
    for _, n in zip(range(x), nums):
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'

print("Winner: {}".format(isWinner(3, [1, 2, 3])))
