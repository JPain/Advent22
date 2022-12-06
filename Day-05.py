#!/usr/bin/env python3
import os

inputFileName = os.path.basename(__file__).replace('.py', '-input.txt')

def part1():
    stacks = [[] for i in range(9)]
    with open(inputFileName) as fileInput:
        for line in fileInput.readlines():

            if line[0] == '[':
                for i in range(9):
                    cursor = 4 * i
                    if line[cursor] == '[':
                        stacks[i].append(line[cursor + 1])
            
            if line[0] == 'm':
                command = line.replace('move ', '').replace('from ', '').replace('to ', '').split()
                numberToMove = int(command[0])
                fromStackNum = int(command[1]) - 1
                toStackNum = int(command[2]) - 1
                for i in range(numberToMove):
                    extractedItem = stacks[fromStackNum].pop(0)
                    stacks[toStackNum].insert(0,extractedItem)

    result = ''
    for stack in stacks:
        result = result + stack[0]
    print(result)

def part2():
    stacks = [[] for i in range(9)]
    with open(inputFileName) as fileInput:
        for line in fileInput.readlines():

            if line[0] == '[':
                for i in range(9):
                    cursor = 4 * i
                    if line[cursor] == '[':
                        stacks[i].append(line[cursor + 1])
            
            if line[0] == 'm':
                command = line.replace('move ', '').replace('from ', '').replace('to ', '').split()
                numberToMove = int(command[0])
                fromStackNum = int(command[1]) - 1
                toStackNum = int(command[2]) - 1
                extractedItems = []
                for i in range(numberToMove):
                    extractedItems.append(stacks[fromStackNum].pop(0))
                for i in range(numberToMove):
                    stacks[toStackNum].insert(0,extractedItems.pop())

    result = ''
    for stack in stacks:
        result = result + stack[0]
    print(result)

if __name__ == "__main__":
    part1()
    part2()
