f = open("puzzle.txt", "r")
rawData = f.read()
f.close()

# ["1", "2", "3"]
# ["2", "3", "1 "]
def starOne():
  #set the data equal to the same variables to make comparison easier:
  #Rock = A X = 1, Paper = B Y = 2, Scissors = C Z = 3
  cleanedData = rawData.replace("A", "1").replace("B", "2").replace("C", "3").replace("X", "1").replace("Y", "2").replace("Z", "3")
  gamesList = [item.split(" ") for item in cleanedData.split("\n")]
  sum = 0
  for game in gamesList:
    #expected count for player two wins == player two's play
    if (int(game[0])%3 + 1) == int(game[1]): sum += (6 + int(game[1]))
    elif game[0] == game[1]: sum+= 3+ int(game[0])
    else: sum+=int(game[1])
  return sum

def starTwo():
  cleanedData = rawData.replace("A", "1").replace("B", "2").replace("C", "3")
  gamesList = [item.split(" ") for item in cleanedData.split("\n")]
  sum = 0
  for game in gamesList:
    #X = loose => Shift numbers one space over to left
    if game[1] == "X": sum+= (int(game[0])-2)%3 + 1
    #Y = draw => Number is the played number
    elif game[1] == "Y": sum+= 3 + int(game[0])
    #Z = win => shift numbers one space over to right
    elif game[1] == "Z": sum += 6 + (int(game[0]) )%3 + 1
  return sum
  
print(starOne())
print(starTwo())
