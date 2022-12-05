#!/usr/bin/env python3

def main():
    sumprio = 0
    with open('input.txt') as f:
        for line in f: # assuming No. of chars is even in all cases
            comp1 = line[:len(line)//2]
            comp2 = line[len(line)//2:-1] # cut newline
            # print(comp1, len(comp1), comp2, len(comp2))
            for ch in comp1:
                if ch in comp2 :
                    if ch.islower():
                        priority = ord(ch) - 96 # 'a' is 97 in ASCII, minus it's prio 1 gives 96 as base number
                    else: 
                        priority = ord(ch) - 38 # 'A' is 65 in ASCII, minus it's prio 27 gives 38 as base number
                    # print("common item:", ch, "prio:", priority)
                    sumprio += priority
                    break
    print("Sum of priorities:", sumprio)

if __name__ == "__main__":
    main()

