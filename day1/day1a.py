#!/usr/bin/env python3

import os

def main():
    maxcalories = 0
    currentcalories = 0
    with open("input.txt") as f:
        for myline in f:
            if myline != '\n':
                currentcalories += int(myline)
            else:
                if currentcalories > maxcalories :
                    maxcalories = currentcalories
                    # print("New max: ", maxcalories)
                # print("This bag contains", currentcalories, "calories")
                currentcalories = 0

    print("Max calories:", maxcalories)

if __name__ == "__main__":
    main()

