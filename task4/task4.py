import sys
import os

dir = os.path.dirname(sys.argv[0])

mass = []
f = open(os.path.join(dir, sys.argv[1]))
for line in f:
   mass = mass + line.split()
f.close()

sum_mass = 0 
for x in mass:
    sum_mass += int(x)
mid_val = sum_mass/len(mass)
mid_val = round(mid_val)

count = 0
for x in mass:
    count += abs(int(x) - mid_val)

print(count)
