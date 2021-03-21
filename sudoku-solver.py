# imports
import pprint

# initializing placeholder puzzle array[array]
puzzle = [[0 for x in range(9)] for y in range(9)]
# pprint.pprint(puzzle)

# printing filled grid
def printFilled(p):
  print("-"*19)
  for i in range(9):
    for j in range(9):
      print("|"+str(p[i][j]), end="")
    print()
    print("-"*19)
  return 0

# does it work?
printFilled(puzzle)
# ok it works

