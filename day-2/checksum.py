#!/usr/bin/env python3
import itertools

def checksum(matrix):
    sum = 0
    for row in matrix:
        sum += max(row) - min(row)
    return sum

def checksum_from_file(filepath):
    with open(filepath) as f:
        matrix = [[int(char) for char in list(line.split())] for line in f.readlines()]
        return checksum(matrix)

def checksum_divisable(matrix):
    sum = 0
    for row in matrix:
        sum += max([int(a / b) if a % b == 0 else 0 
                    for a, b in itertools.product(row, repeat=2)])
    return sum

def checksum_divisable_from_file(filepath):
    with open(filepath) as f:
        matrix = [[int(char) for char in list(line.split())] for line in f.readlines()]
        return checksum_divisable(matrix)