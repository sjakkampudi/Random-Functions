import itertools

factorization = []

# returns a list of prime factors of a given 
# number with no repeats
def prime_factorization(num):
	pfactorization = []

	for i in range(2, num):
		while num % i == 0:
			num = num/i
			pfactorization.append(i)

		if num == 1:
			break

	#set() gets rid of repeated factors
	return list(set(pfactorization))

# counts the number of numbers <= num
# such that they are divisible by 
# the factor(s) in the given subset s1
def count_intersection(s1, num):
	subset = list(s1)
	product = 1

	for i in subset:
		product *= i

	return num/product

# sums the counts in subsets of size i
def sum_intersections(num):
	sum = 0

	for i in range(1,len(factorization)+1):
		intersections = list(itertools.combinations(factorization, i))
		for tup in intersections:
			if i%2:
				sum += count_intersection(tup, num)
			else:
				sum -= count_intersection(tup, num)

	return sum

num = 1

#-----------------Script-------------------
while(num > 0):
	num = int(input("Enter an integer (0 to quit): "))
	factorization = prime_factorization(num)

	if (num == 0):
		pass
	# prints num-1 if num is prime
	elif len(factorization) == 0:
		print(num-1)
	else:
		print(int(num - sum_intersections(num)))

#------------------------------------------