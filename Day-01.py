#!/usr/bin/env python3
import time

def part1():
    print('You wanna know the elf with most beef? We\'ve got you')
    beefiestElf = 0
    howBeefIsElf = 0

    with open('Day-01-input.txt') as fileInput:
        for line in fileInput.readlines():
            line = line.strip()
            if line == '':
                if howBeefIsElf > beefiestElf:
                    beefiestElf = howBeefIsElf
                howBeefIsElf = 0
            else:
                howBeefIsElf = howBeefIsElf + int(line)
    print('Result: ' + str(beefiestElf))
    if beefiestElf > 9000:
        print('That\'s a lot of beef!')

def part2():
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
        result = listOfBeef[0] + listOfBeef[1] + listOfBeef[2]
        print('Result: ' + str(result))
        if result > 99999:
            print('These elfs have too much beef.')

if __name__ == "__main__":
    print(time.process_time_ns())
    part1()
    print('Part 1 time: ' + str(time.process_time_ns()))
    part2()
