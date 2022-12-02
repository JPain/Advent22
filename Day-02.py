#!/usr/bin/env python3
import math

def part1():
    throws = {
        'A': {'X': 4, 'Y': 8, 'Z': 3},
        'B': {'X': 1, 'Y': 5, 'Z': 9},
        'C': {'X': 7, 'Y': 2, 'Z': 6}
    }
    score = 0
    with open('Day-02-input.txt') as fileInput:
        for line in fileInput.readlines():
            choices = line.strip().split(' ')
            score = score + throws[choices[0]][choices[1]]
    print(score)

def part2():
    throws = {
        'A': {'X': 3, 'Y': 4, 'Z': 8},
        'B': {'X': 1, 'Y': 5, 'Z': 9},
        'C': {'X': 2, 'Y': 6, 'Z': 7}
    }
    score = 0
    with open('Day-02-input.txt') as fileInput:
        for line in fileInput.readlines():
            choices = line.strip().split(' ')
            score = score + throws[choices[0]][choices[1]]
    print(score)


if __name__ == "__main__":
    part1()
    part2()