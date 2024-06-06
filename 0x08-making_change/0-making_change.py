#!/usr/bin/python3
"""makeChange module"""


def makeChange(coins, total):
    """ determine the fewest number of
    coins needed to meet a given amount total."""
    # Initialize an array to store the minimum number of coins for each value
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed for total value 0

    for coin in coins:
        for value in range(coin, total + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)

    # If the total cannot be met, return -1
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
