# print the mean of the numbers given as arguments

import sys

sum = 0

if len(sys, argv) == 1:
    print "Error: no arguments given."
    sys.exit()

for num in sys.argv[1:]:
    sum +=float(num)

print sum/(len(sys.argv)-1)

