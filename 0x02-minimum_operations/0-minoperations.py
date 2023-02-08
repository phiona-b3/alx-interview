#!/usr/bin/python3
'''minumun operations'''


def minOperations(n):
    '''method to calcualte the fewest number of operations'''
    count = 0
    div = 2
    if n <= 1:
        return 0
    while n > 1:
        if (n % div == 0):
            n = n / div
            count = count + div
        else:
            div += 1
    return count
