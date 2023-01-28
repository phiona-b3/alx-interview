#!/usr/bin/python3
'''interview question'''

def pascal_triangle(n):
    '''returns pascal triangle'''
    list = []
    if n == 0:
        return list
    list = [[] for i in range (n)]
    for i in range(n):
        for j in range(i+1):
            if (j < i):
                if (j == 0):
                    list[i].append(1)
                else:
                    list[i].append(list[i - 1][j] + list[i-1][j-1])
            elif (j == 1):
                list[i].append(1)
    return list