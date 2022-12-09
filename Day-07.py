#!/usr/bin/env python3
import os

inputFileName = os.path.basename(__file__).replace('.py', '-input.txt')

def part1():
    with open(inputFileName) as fileInput:
        files = {}
        directories = {}
        currentDirectory = ''
        for line in fileInput.readlines():
            line = line.strip()
            if line[0] == '$':
                if line[2:4] == 'cd':
                    if line[5:] == '/':
                        currentDirectory = '/'
                    elif line[5:] == '..':
                        currentDirectory = currentDirectory[:currentDirectory.rindex('/',0,len(currentDirectory)-1)+1]
                    else:
                        currentDirectory = currentDirectory + line[5:] + '/'
                    if not currentDirectory in directories:
                        directories[currentDirectory] = 0
                elif line[2:4] == 'ls':
                    continue
                else:
                    print('Unexpected command {0}'.format(line))
            elif line[0] == 'd':
                continue
            elif line[0].isnumeric():
                files[currentDirectory + line[line.index(' ')+1:]] = int(line[:line.index(' ')])
                directories[currentDirectory] = directories[currentDirectory] + int(line[:line.index(' ')])
        for item in directories:
            for secondItem in directories:
                if secondItem == item:
                    continue
                if secondItem.find(item) == 0:
                    directories[item] = (directories[item] + directories[secondItem])
        sumTotal = 0
        for dire, size in directories.items():
            if size < 100000:
                print('found ' + str(size))
                sumTotal = sumTotal + size
        print(sumTotal)
        # Oh my, that got very very ugly

        

def part2():
    with open(inputFileName) as fileInput:
        for line in fileInput.readlines():
            print('nothing')
            # Logic here

if __name__ == "__main__":
    part1()
    # part2()
