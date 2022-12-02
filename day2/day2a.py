#!/usr/env/python3

def main ():
  scoredict = { 'A X\n':4, 'A Y\n':8, 'A Z\n':3, 'B X\n':1, 'B Y\n':5, 'B Z\n':9, 'C X\n':7, 'C Y\n':2, 'C Z\n':6 }
  score = 0
  with open("input.txt") as f:
    for line in f:
      score += scoredict[line]
  
  print("Final score:", score)

if __name__ == '__main__' :
  main()
