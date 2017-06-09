from math import log

PHI = (1 + 5**0.5)/float(2)
LOG_5 = log(5, PHI)/float(6)
def largest_even_fib_under_n(n):
    return int(LOG_5 + log(n, PHI)/float(3))


def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)
            
def sum_even_fib_naive(limit):
    n = total = 0
    while fib(n) < limit:
        n += 1
        if fib(n) % 2 == 0:
            total += fib(n)
    return total


def sum_even_fib_under_n(n):
    if n > 10**15:
        return sum_even_fibbonaci(n)
    fib_max_index = largest_even_fib_under_n(n)
    phi = ((1+5**0.5)/float(2))

    def sum_phi(k, positive=True):
        if positive:
            i = 1
        else:
            if k > 10:
                return (5**0.5-1)/float(4)
            i = -1
        phi_3 = phi**(3*i)
        return phi_3*(1 - (i*phi_3)**k)/float(1 - phi_3)
    total = sum_phi(fib_max_index) + sum_phi(fib_max_index, False)
    return int(total/float(5**0.5))


def sum_even_fibbonaci(limit, F_1 = 1, F_2 = 2):
    total = 0
    k = 2
    while F_2 < limit:
        k += 1
        if F_2 % 2 == 0:
            total += F_2
        F_3 = F_2 + F_1
        F_1 = F_2
        F_2 = F_3
    print k
    return total


def sum_even_fibbonaci_faster(max_value, F_1 = 1, F_2 = 2):
    total = 0
    while F_2 < max_value:
        total += F_2
        for _ in range(3):
            F_2, F_1 = F_1 + F_2, F_2
    return total


def sum_even_fast(limit):
    a, b = 0, 2
    total = 0
    while b < limit:
        total += b
        a, b = b, 4 * b + a
    return total

def sum_even_fastest(limit):
    a, b = 0, 2
    while b < limit:
        a, b = b, 4 * b + a
    return (a + b - 2) / 4


if __name__ == "__main__":

    print largest_even_fib_under_n(4*10**6)
    print
    print sum_even_fib_naive(4*10**6)
    print sum_even_fibbonaci_faster(4*10**6)
    print sum_even_fibbonaci(4*10**6)
    # print sum_even_fib_under_n(100)
    print sum_even_fast(4*10**6)
    print sum_even_fastest(4*10**6)
    print

    import timeit
    # times = 10
    # t1 = timeit.timeit("sum_even_fibbonaci(2*10**60)",
    #                    setup="from __main__ import sum_even_fibbonaci", number=times)/float(times)
    # t2 = timeit.timeit("sum_even_fib_under_n(2*10**60)",
    #                    setup="from __main__ import sum_even_fib_under_n", number=times)/float(times)
    # t3 = timeit.timeit("sum_even_fast(2*10**60)",
    #                    setup="from __main__ import sum_even_fast", number=times)/float(times)
    # t4 = timeit.timeit("sum_even_fastest(2*10**60)",
    #                    setup="from __main__ import sum_even_fastest", number=times)/float(times)
    # print ''' 
    # {} ms 
    # {} ms 
    # {} ms 
    # {} ms 
    # maths was {} times faster than naive
    # fastest was {} times faster than naive
    # fastest was {} times faster than maths
    # '''.format(1000*t1, 1000*t2, 1000*t3, 1000*t4, t1/float(t2), t1/float(t4), t2/float(t4))