from math import factorial
import timeit

"Factorial digit sum"

"Problem 20"

"n! means n x (n - 1) x ... x 3 x 2 x 1"

"For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,"
"and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27."

"Find the sum of the digits in the number 100!"


def digit_sum_fast(num):
    return sum(map(int, str(num)))

if __name__ == '__main__':

	# One liner
	num = 100
	# print timeit.timeit(lambda: sum(int(digit) for digit in str(factorial(num))), number = 10000)
	# print timeit.timeit(lambda: digit_sum_fast(factorial(num)), number = 10000)
	print digit_sum_fast(factorial(num))
	
