#!/usr/bin/env python3

def main():
    contain = 0
    with open('input.txt') as f:
        for line in f:
            sections = line[:-1].split(",") # avoid newline
            elf1 = sections[0].split("-")
            elf2 = sections[1].split("-")
            if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]) :
                # print("First range contains second:",elf1,elf2)
                contain += 1
            elif int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1]) :
                # print("Second range contains first:",elf1,elf2)
                contain += 1
            else:
                # print("No contain:",elf1,elf2)
                pass

    print("Containing pairs:", contain)

if __name__ == "__main__":
    main()

