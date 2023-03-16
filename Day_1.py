#reading file
f = open("puzzle.txt", "r")
elfFood = [int(x) for x in f.read().replace("\n","\n0").split()]
f.close()

#global variable
sumElfFood = []

#function for the first star
def starOne():
  tempSum = 0
  #iterating through and summing them up, storing in sumElfFood
  for x in elfFood:
    if x == 0: 
      sumElfFood.append(tempSum)
      tempSum = 0
    else: tempSum+=x
  return max(sumElfFood)

#function for the second star
def starTwo():
  copyElfList = list(sumElfFood)
  copyElfList.sort(reverse=True)
  print(copyElfList)
  return (copyElfList[0]+copyElfList[1]+copyElfList[2])

print(starOne())
print(starTwo())
