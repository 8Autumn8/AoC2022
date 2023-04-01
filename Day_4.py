f = open("puzzle.txt", "r")
rawData = f.read()
f.close()

#Scenerio: In "[a,b],[c,d]" does [a,b] contain [c,d] or [c,d] contain [a,b]? where a,b,c,d are ints
def starOne():
  count = 0
  cleanedData = [list.split(",") for list in rawData.split("\n")]
  for pair in cleanedData:
    elfOneStr, elfTwoStr = pair[0].split("-") , pair[1].split("-")
    elfOne, elfTwo = [eval(i) for i in elfOneStr] , [eval(i) for i in elfTwoStr]
    #[a,b],[c,d]
    #compare the maximums and minimums of a function, looking a and c, and then b and d
    if (elfOne[0]>=elfTwo[0] and elfOne[1]<=elfTwo[1]) or (elfOne[0]<=elfTwo[0] and elfOne[1]>=elfTwo[1]):
      count+=1
  return count

#Scenerio: Does "[a,b],[c,d]" overlap in any way? where a,b,c,d are ints
def starTwo():
  count = 0
  cleanedData = [list.split(",") for list in rawData.split("\n")]
  for pair in cleanedData:
    elfOneStr, elfTwoStr = pair[0].split("-") , pair[1].split("-")
    elfOne, elfTwo = [eval(i) for i in elfOneStr] , [eval(i) for i in elfTwoStr]
    #[a,b],[c,d]
    #compare the maximums and minimums of a function, looking a and d, and then b and c
    if (elfOne[0]>=elfTwo[1] and elfOne[1]<=elfTwo[0]) or (elfOne[0]<=elfTwo[1] and elfOne[1]>=elfTwo[0]):
      count+=1
  return count

print(starOne())
print(starTwo())
