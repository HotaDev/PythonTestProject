import sys
import os

dir = os.path.dirname(sys.argv[0])

f = open(os.path.join(dir, input('Введите название файла с данными окружности ')))
center = f.readline().split(' ')
r = int(f.readline())
f.close()
dot = []
f = open(os.path.join(dir, input('Введите название файла с точками ')))
for line in f:
    dot = dot + line.split(' ')   
f.close() 
i = 0
while (i != len(dot)):
    pos = (int(dot[i]) - int(center[0]))**2 + (int(dot[i + 1]) - int(center[1]))**2
    if pos == r ** 2:
        print(0)
    elif pos > r ** 2:
        print(2)
    else:
        print(1)
    i += 2