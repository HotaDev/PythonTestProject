import sys

n = int(sys.argv[1])
m = int(sys.argv[2])
way = '1'
currPath = 1
while 1:
    if (currPath + m - 1) > n:
        currPath = currPath + m - 1 - n
    else:
        currPath = currPath + m - 1
    if currPath == 1:
        break
    way = way + str(currPath)
print(way)
    