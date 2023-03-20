f = open("puzzle.txt", "r")
rawData = f.read()
f.close()

def starOne():
  sum = 0
  compartments = rawData.split("\n")
  for item in compartments:
    res_first, res_second = item[:len(item)//2], item[len(item)//2:]
    s1_chars, s2_chars  = set(res_first), set(res_second)
    ascii = ord(list(s1_chars.intersection(s2_chars))[0])

    #converting ascii to values a-z to 1-26 and A-Z to 27-52
    if ascii > 96: sum += ascii-96
    else: sum += ascii-38
  return sum

def starTwo():
  sum = 0
  i = 0
  compartments = rawData.split("\n")
  while (i < len(compartments)-2):
    res_first, res_second, res_third = compartments[i], compartments[i+1], compartments[i+2]
    s1_chars, s2_chars, s3_chars  = set(res_first), set(res_second), set(res_third)
    ascii = ord(list(s1_chars.intersection(s2_chars, s3_chars))[0])
    
    #converting ascii to values a-z to 1-26 and A-Z to 27-52
    if ascii > 96: sum += ascii-96
    else: sum += ascii-38
    i+=3
  return sum

print(starOne())
print(starTwo())
