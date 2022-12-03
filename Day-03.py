#!/usr/bin/env python3

def part1():
    # With input of strings, find duplicate characters between the two halfs.
    # Calculate a score from the characters.
    score = 0
    with open('Day-03-input.txt') as fileInput:
        for line in fileInput.readlines():

            # Split the strings exactly into 2. They will always split evenly.
            firstCompartment = line.strip()[:int(len(line)/2)]
            secondCompartment = line.strip()[int(len(line)/2):]

            # Sets are collections that can't have duplicates
            firstUnique = set()
            secondUnique = set()

            # Turn strings into sets
            for x in firstCompartment:
                firstUnique.add(x)
            for x in secondCompartment:
                secondUnique.add(x)
            
            # Find the character that exists in both sets
            outlierSet = firstUnique.intersection(secondUnique)

            # Extract the string from the returned set
            outlier = outlierSet.pop()

            # Turn the character into a score value and add to total
            # We use ord to find the ASCII code for the letter and
            # adjust it to fit the scoring rule.
            if outlier.isupper():
                score = score + (ord(outlier) - 38)
            else:
                score = score + (ord(outlier) - 96)
        # Output total score
        print(score)

def part2():
    # Now, rather than splitting, do it for every 3 lines of input
    with open('Day-03-input.txt') as fileInput:

        # Let's get input as a list of strings
        lines = fileInput.read().strip().split('\n')

        # Lets create lists of 3x strings inside a list
        groups = []
        while len(lines) > 0:
            groups.append([lines.pop(), lines.pop(), lines.pop()])

        # Now for each list of 3, do the comparisons and scoring
        score = 0
        for group in groups:
            firstElf = set()
            secondElf = set()
            thirdElf = set()

            for x in group[0]:
                firstElf.add(x)
            for x in group[1]:
                secondElf.add(x)
            for x in group[2]:
                thirdElf.add(x)
            
            outlierSet = firstElf.intersection(secondElf, thirdElf)

            outlier = outlierSet.pop()

            if outlier.isupper():
                score = score + (ord(outlier) - 38)
            else:
                score = score + (ord(outlier) - 96)

        print(score)

if __name__ == "__main__":
    part1()
    part2()