#!/usr/bin/env python3

def crane(myarray, source, dest):
    if len(myarray[source]) > 0 :
        myletter = myarray[source].pop()
        # print('Got crate:',myletter)
        myarray[dest].append(myletter)

def main():
    stack = [ 
        ['X'], # placeholder 0th row
        ['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q'],
        ['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J'],
        ['F', 'B', 'H', 'W', 'P', 'M', 'Q'],
        ['V', 'S', 'T', 'D', 'F'],
        ['Q', 'L', 'D', 'W', 'V', 'F', 'Z'],
        ['Z', 'C', 'L', 'S'],
        ['Z', 'B', 'M', 'V', 'D', 'F'],
        ['T', 'J', 'B'],
        ['Q', 'N', 'B', 'G', 'L', 'S', 'P', 'H'],
        ]
    
    with open('input.txt') as f:
        for line in f:
            # move 1 from 8 to 1
            myinput = line.split(' ')
            howmany = int(myinput[1])
            source = int(myinput[3])
            dest = int(myinput[5])
            for lift in range(0,howmany):
                crane(stack, source, dest)
            
    print(stack)
    print('Top crates:')
    for i in range(1,10):
        if len(stack[i]) > 0 :
            print(stack[i].pop(), end='')

if __name__ == '__main__':
    main()