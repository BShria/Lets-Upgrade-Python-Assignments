# find the character with the maximum frequency from the input string

s = input("Enter the lottery string: ")

# using list
freqList = [0] * 26

for i in s:
  freqList[(ord(i) - 97)] += 1

ans = freqList.index(max(freqList))
print(chr(ans + 97)) 
# chr function converts integer to character

# using dictionary
freqDict = {}

for i in s:
  freqDict[i] = freqDict.get(i,0) + 1

maxFreq = 0
ansChar = '$'
for i in freqDict.items():
  if(i[1] > maxFreq):
    maxFreq = i[1]
    ansChar = i[0]

print(ansChar)

# Input: helloworld
# Output: 
# l
# l
