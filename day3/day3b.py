#!/usr/bin/env python3

def main():
    sumprio = 0
    mygroup = []
    with open('input.txt') as f:
        for line in f: # assuming No. of chars is even in all cases
            backpack = line[:-1] # cut newline
            mygroup.append(backpack)
            if len(mygroup) >= 3:
                # print(mygroup)
                try:
                    for ch1 in mygroup[0]:
                        for ch2 in mygroup[1]:
                            if ch1 == ch2 :
                                for ch3 in mygroup[2]:
                                    if ch1 == ch2 and ch1 == ch3 :
                                        # print('Common item:', ch1)
                                        if ch1.islower():
                                            priority = ord(ch1) - 96 # 'a' is 97 in ASCII, minus it's prio 1 gives 96 as base number
                                        else: 
                                            priority = ord(ch1) - 38 # 'A' is 65 in ASCII, minus it's prio 27 gives 38 as base number
                                        # print('priority:',priority)
                                        sumprio += priority
                                        raise StopIteration
                except StopIteration:
                    pass
                mygroup = []

    print("Sum of priorities:", sumprio)

if __name__ == "__main__":
    main()

