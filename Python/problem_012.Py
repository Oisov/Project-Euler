from faktorisering import factorization
from collections import Counter
from math import log, sqrt

divisors_ = Counter()

def divisors(div):
	if divisors_[div] == 0:
		facs = factorization(div)
		divs = 1
		for key in facs:
			divs *= (facs[key]+1)
		divisors_[div] = divs
	return divisors_[div]


def triangular_divisors(limit):
	if limit < 100:
		n = int(limit/2)
	else:
		n = 2*limit
	div = divisors(n*(n+1)/2)
	while div < limit:
		n += 1
		if n % 2 == 0:
			div = divisors(n/2)*divisors(n+1)
		else:
			div = divisors(n)*divisors((n+1)/2)
	return n, div


if __name__ == '__main__':

	n, div = triangular_divisors(500)

	print 'tri(',n,') =', (n+1)*n/2
	print 'divisors = ', div