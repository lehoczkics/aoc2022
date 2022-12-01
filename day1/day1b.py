#!/usr/bin/env python3

import os

def main():
    allcalories = []
    currentcalories = 0
    with open("input.txt") as f:
        for myline in f:
            if myline != '\n':
                currentcalories += int(myline)
            else:
                # print("This bag contains", currentcalories, "calories")
                allcalories.append(currentcalories)
                currentcalories = 0
    
    allcalories.sort(reverse = True)
    top3 = allcalories[0] + allcalories[1] + allcalories[2]
    print("Calories of top3 bag:",top3)


if __name__ == "__main__":
    main()

