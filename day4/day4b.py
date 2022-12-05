#!/usr/bin/env python3

def main():
    overlap = 0
    with open('input.txt') as f:
        for line in f:
            sections = line[:-1].split(",") # avoid newline
            elf1 = sections[0].split("-")
            elf2 = sections[1].split("-")
            if int(elf1[1]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1]) :
                overlap += 1
            else:
                pass

    print("Overlapping pairs:", overlap)

if __name__ == "__main__":
    main()

