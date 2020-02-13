# Author: Akshith Gara
# https://open.kattis.com/problems/bijele
import sys

inputList = sys.stdin.readline()
inputList = inputList.split()

for i in range(len(inputList)):
    inputList[i] = int(inputList[i])

correctValues = [1,1,2,2,2,8]

outList = []
for i in range(len(inputList)):
    if correctValues[i] != inputList[i]:
        outList.append(correctValues[i]-inputList[i])
    else:
        outList.append(0)

finalString = ' '.join([str(x) for x in outList])
print(finalString)
