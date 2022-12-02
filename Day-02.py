#!/usr/bin/env python3
import math

def part1():
    # Calculate the score of the given input's Rock, Paper Scissors matches.
    # Where A B C is an opponant's Rock, Paper Scissors choice, and X Y Z is your choice;
    # Based on a scoring system of Win = 6, Tie = 3, Lose = 0 plus a bonus of what you
    # chose as Rock = 1, Paper = 2, and Scissors = 3;

    throws = {
        'A': {'X': 4, 'Y': 8, 'Z': 3},
        'B': {'X': 1, 'Y': 5, 'Z': 9},
        'C': {'X': 7, 'Y': 2, 'Z': 6}
    }

    # I tried to come up with a fancy mathmatical calculation to solve the result
    # of a Rock Paper Scissor match. I tried converting the choice into a number,
    # and running an operation on that number to determin the result. Like, if
    # Rock = 1, and Scissors = 2, then calculate 1 + 2. If result is 3, then win.
    # 
    # I couldn't find a single way to calculate the result mathmatically.
    #
    # So I ended up hardcoding the results. I'm not happy about it, but it works.

    score = 0
    with open('Day-02-input.txt') as fileInput:
        for line in fileInput.readlines():
            choices = line.strip().split(' ')
            score = score + throws[choices[0]][choices[1]]
    print(score)

def part2():
    # Calculate the score if X = lose, Y = tie, and Z = win
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