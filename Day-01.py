#!/usr/bin/env python3
import time

def part1():
    # Given input of groups of numbers, find the group with the highest sum.
    print('You wanna know the elf with most beef? We\'ve got you')
    beefiestElf = 0
    howBeefIsElf = 0

    with open('Day-01-input.txt') as fileInput:
        for line in fileInput.readlines():
            line = line.strip()
            if line == '':
                # I realised afterwards that this may not trigger after the last group
                # if the input doesn't have a blank line at the end, so the last group
                # may not get compared and added to the highest number total.
                if howBeefIsElf > beefiestElf:
                    beefiestElf = howBeefIsElf
                howBeefIsElf = 0
            else:
                howBeefIsElf = howBeefIsElf + int(line)
    print('Result: ' + str(beefiestElf))
    if beefiestElf > 9000:
        print('That\'s a lot of beef!')

def part2():
    # Given input of groups of numbers, find the top 3 groups with the highest 
    # sums and return sum of the 3 groups.
    print('Oh, you want the top 3 combined now? How very agile of you.')
    howBeefIsElf = 0
    listOfBeef = []

    with open('Day-01-input.txt') as fileInput:
        for line in fileInput.readlines():
            line = line.strip()
            if line == '':
                listOfBeef.append(howBeefIsElf)
                howBeefIsElf = 0
            else:
                howBeefIsElf = howBeefIsElf + int(line)
        listOfBeef.sort(reverse=True)
        # I don't like adding the whole input into a list and running a
        # sort on the whole thing. It's quite wasteful of memory.
        # However, I'm doing one of these every day. They can't all be 
        # winners.
        result = listOfBeef[0] + listOfBeef[1] + listOfBeef[2]
        print('Result: ' + str(result))
        if result > 99999:
            print('These elfs have too much beef.')

if __name__ == "__main__":
    print(time.process_time_ns())
    # I wanted to compare running time with a friend's soloution.
    part1()
    print('Part 1 time: ' + str(time.process_time_ns()))
    # It was coming out as taking 0ns to run. I might not understand
    # the function well enough.
    part2()
