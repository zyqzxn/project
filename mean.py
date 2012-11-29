# print the mean of the numbers given as arguments

import sys

#define the variables to store the sum
sum = 0
n = 0

#check the files

#get the values from the second to the end
for num in open(sys.argv[1]):
    sum +=float(num)
    n += 1

#zyq add again

print sum/n

