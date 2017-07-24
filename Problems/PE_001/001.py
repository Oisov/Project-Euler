#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get

    3, 5, 6 and 9.

The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

from itertools import combinations
from fractions import gcd

lcm_dict = {(): 1}


def lcm(a, b):
    return a * b // gcd(a, b)


def lcm_list(perm):
    l = lcm(lcm_dict[perm[:-1]], perm[-1])
    lcm_dict[perm] = l
    return l


def remove_multiples(divisors):
    # Directly from Joe Wallis's answer
    new_divisors = []
    divisors = sorted(set(divisors))
    for divisor in divisors:
        if not any(divisor % d == 0 for d in new_divisors):
            new_divisors.append(divisor)
    return new_divisors


def sum_divisible_by_k(k, start, stop):
    sum_start = -(-start // k)
    sum_stop = (stop - 1) // k
    return int(0.5*k*(sum_stop+sum_start)*(sum_stop-sum_start+1))


def sum_divisible_fast(div=[3, 5], stop=100, start=1):
    '''
    Finds all numbers divisible by the numbers in div
    from start to stop. This is done using the inclusion-exclusion principle
    https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle
    sum_divisible_fast([2, 3], 0, 10) = 32
    Since 2 + 3 + 4 + 6 + 8 + 9 = 32.
    '''
    divisors = remove_multiples(div)
    total = 0

    j = 1
    for i in xrange(1, len(divisors)+1):
        for perm in combinations(divisors, i):
            product = lcm_list(perm)
            total += j*sum_divisible_by_k(product, start, stop)
        j = -j

    return total


def sum_divisible_naive(divisors=[3, 5], stop=100, start=1):
    count = 0
    for num in xrange(start, stop):
        for d in divisors:
            if num % d == 0:
                count += num
                break
    return count


if __name__ == "__main__":

    print sum_divisible_fast([2, 3], 10)
    print sum_divisible_naive([2, 3], 10)
    print
    print sum_divisible_naive([3, 15], 100000)
    print sum_divisible_fast([3, 15], 100000)

    import timeit

    times = 10
    t1 = timeit.timeit("sum_divisible_naive([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 10**6)",
                       setup="from __main__ import sum_divisible_naive", number=times)/float(times)
    print "Naive: ", t1*1000
    t2 = timeit.timeit("sum_divisible_fast([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 10**6)",
                       setup="from __main__ import sum_divisible_fast", number=times)/float(times)
    print "Optimized: ", t2*1000
    print "The optimized code was {} times faster than the naive".format(t1/float(t2))
