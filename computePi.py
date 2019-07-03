# File: computePi.py
# Author: Pete Sripitak
# Uses the dart throwing algorithm to compute pi.

#!/usr/local/bin/python3.2

import sys, random, math

n = int(sys.argv[1])
hit = 0.0

for i in range(n):
	x = random.random()
	y = random.random()
	dist = math.sqrt( x*x + y*y )
	if dist <= 1:
		hit += 1.0
		
ratio = hit / n
print('\nThe hits ratio is ', ratio)
value = ratio * 4
print('The estimated value of pi is ', value,'\n')
