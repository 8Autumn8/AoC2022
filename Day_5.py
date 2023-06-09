f = open("puzzle.txt", "r")
rawData = f.read()
f.close()

#Changes based on input data
numLines = 9
indexInRow = numLines * 3 + (numLines-2)
cleanedData = rawData.split("\n")

#process first [numLines] of input to read the original crates order in data
def getCrates():
  stackCount = 0
  allCrates = [None] * numLines
  for column in range(1, indexInRow, 4):
    stack = []
    for row in range(numLines-1, -1, -1):
      if (cleanedData[row][column] != " "): 
        stack.append(cleanedData[row][column])
    allCrates[stackCount] = stack
    stackCount+=1
  return allCrates

#Clean inputs of move commands from data
def getMoveInput():
  splitSpaces = [list.split(" ") for list in cleanedData[numLines+2:]]
  allMoves = []
  for line in splitSpaces:
    move = [int(line[1]), int(line[3]), int(line[5])]
    allMoves.append(move)
  return allMoves

#Iterates through and moves crates ONE at a time
def starOne():
  allCrates = getCrates()
  allMoves = getMoveInput()
  for i in range (0, len(allMoves)):
    for numPop in range (0, allMoves[i][0]):
      popValue = allCrates[allMoves[i][1]-1].pop()   
      allCrates[allMoves[i][2]-1].append(popValue)
  #Grabs top crates of each stack and returns it
  return "".join([e.pop() for e in allCrates])

#Iterates through and moves crates MULTIPLE at a time
def starTwo():
  allCrates = getCrates()
  allMoves = getMoveInput()
  for i in range (0, len(allMoves)):
    cratesMoving = []
    for numPop in range (0, allMoves[i][0]):
      cratesMoving.append(allCrates[allMoves[i][1]-1].pop())
    #Reverses list then appends.
    cratesMoving.reverse()
    allCrates[allMoves[i][2]-1] += cratesMoving
  #Grabs top crates of each stack and returns it
  return "".join([e.pop() for e in allCrates])
  
print(starOne())
print(starTwo())
