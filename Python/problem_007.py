#!/usr/bin/env python
from math import log
from faktorisering import primesbelow
from primesieve import nth_prime

def ith_fast(n):
    stop = int(n*(log(n) + log(log(n) - 1 + 1.8*log(log(n))/float(log(n)))))
    sieve = primesbelow(stop)
    return sieve[n-len(sieve)-1]

if __name__ == "__main__":
    import timeit
    limit = 10001
    print ith_fast(limit)
    print nth_prime(limit)
    times = 50
    t1 = timeit.timeit("ith_fast(1000001)", setup="from __main__ import ith_fast", number = times)/float(times)
    t2 = timeit.timeit("nth_prime(1000001)", setup="from __main__ import nth_prime", number = times)/float(times)

    print "My solution used: ", 1000*t1, "ms"
    print "The C++ solution used:  ", 1000*t2, "ms"

    print "The C++ solution was:   ", t1/float(t2), "times faster than mine."