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
        # more stuff here
        

def part2():
    with open(inputFileName) as fileInput:
        for line in fileInput.readlines():
            print('nothing')
            # Logic here

if __name__ == "__main__":
    part1()
    # part2()
