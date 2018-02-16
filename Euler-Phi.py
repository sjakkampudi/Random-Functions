import itertools
import math

factorization = []

def prime_factorization(num):
	pfactorization = []

	for i in range(2, num):
		while num % i == 0:
			num = num/i
			pfactorization.append(i)

		if num == 1:
			i = num

	return pfactorization

def count_intersection(s1, num):
	subset = list(s1)
	product = 1

	for i in subset:
		product *= i

	return num/product

def sum_intersections(num):
	sum = 0
	#factorization = list(set(prime_factorization(num)))

	for i in range(1,len(factorization)+1):
		intersections = list(itertools.combinations(factorization, i))
		for tup in intersections:
			if i%2:
				sum += count_intersection(tup, num)
			else:
				sum -= count_intersection(tup, num)

	return sum;

num = int(input("Enter an integer: "))
factorization = list(set(prime_factorization(num)))

print(num - sum_intersections(num))



