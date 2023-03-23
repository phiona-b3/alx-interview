#!/usr/bin/python3
"""change making problem"""


def makeChange(coins, total):
    """function defining arguments"""
    if total <= 0:
        return 0

    else:
        coins = sorted(coins)
        coins.reverse()
        change = 0
        for coin in coins:
            while coin <= total:
                total -= coin
                change += 1
            if (total == 0):
                return change
        return -1
