
#Testing

import random
import sys

def collatz(num):
	if num == 1:
		return "1"

	if num % 2 == 0:
		return ((str(num) + " -> ") + collatz(int(num/2)))
	else:
		return ((str(num) + " -> ") + collatz(num*3 + 1))

for i in range(9):
	print(collatz(random.randint(1,sys.maxsize)))
	print("\n")