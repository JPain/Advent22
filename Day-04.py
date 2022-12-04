#!/usr/bin/env python3

# For input of pair of number ranges, count how many pairs are completely nested
def part1():

    # Open input file
    with open('Day-04-input.txt') as fileInput:

        # We'll use this to count
        count = 0

        # Read input line by line
        for line in fileInput.readlines():

            # Extract pair of ranges on each line
            pairs = line.strip().split(',')

            # Extract numbers from each pair
            zone1A = int(pairs[0].split('-')[0])
            zone1B = int(pairs[0].split('-')[1])
            zone2A = int(pairs[1].split('-')[0])
            zone2B = int(pairs[1].split('-')[1])

            # Fancy logic that checks if one range is nested inside the other.
            if (zone1A >= zone2A and zone1B <= zone2B) or (zone2A >= zone1A and zone2B <= zone1B):
                count = count + 1
        
        print(count)

# For input of pair of number ranges, count how many overlap at all
def part2():

    # Open input file
    with open('Day-04-input.txt') as fileInput:

        # We'll use this to count
        count = 0

        # Read input line by line
        for line in fileInput.readlines():

            # Extract pair of ranges on each line
            pairs = line.strip().split(',')

            # Extract numbers from each pair
            zone1A = int(pairs[0].split('-')[0])
            zone1B = int(pairs[0].split('-')[1])
            zone2A = int(pairs[1].split('-')[0])
            zone2B = int(pairs[1].split('-')[1])

            # Check if numbers are inside each other's range's
            if isInRange(zone2A, zone2B, zone1A, zone1B) or isInRange(zone1A, zone1B, zone2A, zone2B):
                count = count + 1

        print(count)

# For range, check if input numbers are inside range, and return bool.
def isInRange(rangeStart, rangeEnd, *numbersToCheck):
    # Iterate through input
    for numberToCheck in numbersToCheck:
        # Check if input is between start and end, inclusive
        if (rangeStart <= numberToCheck <= rangeEnd):
            return True
    return False

if __name__ == "__main__":
    part1()
    part2()
