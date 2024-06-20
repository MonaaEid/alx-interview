#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """Prime Game"""
    def generate_primes(n):
        """Helper function to generate
        prime numbers up to n"""
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False

        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i*i, n + 1, i):
                    primes[j] = False

        return [i for i in range(n + 1) if primes[i]]

    def play_round(n):
        """mm"""
        primes = generate_primes(n)
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            for prime in primes:
                if prime > i:
                    break
                if dp[i - prime] == 0:
                    dp[i] = 1

        return dp[n]

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        result = play_round(n)
        if result == 1:
            maria_wins += 1
        elif result == 0:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
