#!/usr/bin/env python3
import os

inputFileName = os.path.basename(__file__).replace('.py', '-input.txt')

def part1():
    with open(inputFileName) as fileInput:
        input = fileInput.readline()
        for i in range(4,len(input)):
            if len(set(input[i-4:i])) == 4:
                print('Found {0} at {1}'.format(input[i-4:i], i))
                return
            

def part2():
    with open(inputFileName) as fileInput:
        input = fileInput.readline()
        for i in range(14,len(input)):
            if len(set(input[i-14:i])) == 14:
                print('Found {0} at {1}'.format(input[i-14:i], i))
                return

if __name__ == "__main__":
    # part1()
    part2()
