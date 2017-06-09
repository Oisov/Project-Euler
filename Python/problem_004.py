import timeit
from primefac import isprime

'''
===============================================

Largest palindrome product
Problem 4

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99. 

Find the largest palindrome made from the product of two 3-digit numbers. 

===============================================
'''


def is_palindrome(number):
    string = str(number)
    return string == string[::-1]


" Solution 0"

def palindrome_product_0(length):
    palindrome_max = 0
    lower = 10**(length-1)+1
    higher = 10**length
    for i in range(lower, higher):
        for j in range(lower, higher):
            if is_palindrome(str(i*j)):
                palindrome = i*j 
                if palindrome > palindrome_max:
                    palindrome_max = palindrome
    return palindrome_max


" Solution 1"

def palindrome_product_1(length):
    palindrome_max = 0
    lower = 10**(length-1)+1
    higher = 10**length
    for i in range(higher, lower, -1):
        for j in range(i, lower, -1):
            if is_palindrome(str(i*j)):
                palindrome = i*j 
                if palindrome > palindrome_max:
                    palindrome_max = palindrome
    return palindrome_max


" Solution 2"

def palindrome_product_2(length):
    palindrome_max = 0
    lower = 10**(length-1)+1
    higher = 10**length
    for i in range(higher, lower, -1):
        if i*i <= palindrome_max:
            break
        for j in range(i, lower, -1):
            if is_palindrome(str(i*j)):
                palindrome = i*j 
                if palindrome > palindrome_max:
                    palindrome_max = palindrome
                    break
    return palindrome_max


" Solution 3"

def palindrome_product_3(n):
    if n == 1: 
        return ((3, 3), 9)

    palindrome = 0
    for i in xrange(10**n - 1, 0, -1):
        # Since all palindromes of length 2n are divisible by 11, either j or i has to be as well"
        if i % 11 == 0:
            j_max = i
            j_range = xrange(j_max + 1, min(palindrome/i, j_max), -1)
        else:
            j_max = 11 * int(i / 11)
            j_range = xrange(j_max, min(palindrome/i, j_max), -11)

        if j_max * i < palindrome:
            break

        for j in j_range:
            product = i * j
            if is_palindrome(product):
                if product > palindrome:
                    palindrome = product
                    break
    return palindrome


" Solution 4"

def cheat_even(num):
    nine = '9'*(num/2)
    num1 = nine + nine
    num2 = nine + '0'*(-1 + num/2) + '1'
    product = nine + '0'*(num) + nine
    return ((int(num1), int(num2)), int(product))


def generate_palindromes(n, increase=False):
    """
    Generates palindromes of length 2n.
    Changing increase to True causes the function to yield the smallest numbers first.
    """
    en = 10 ** n
    en1 = 10 ** (n - 1)
    range_ = xrange(en1, en) if increase else xrange(en - 1, en1 - 1, -1)
    for i in range_:
        i = str(i)
        yield int(i + i[::-1])


def palindrome_product_4(n):
    if n == 1: 
        return ((3, 3), 9)

    en = 10 ** n
    en1 = 10 ** (n - 1)
    for p in generate_palindromes(n):
        p //= 11
        if isprime(p):
            continue
        # Generate numbers such that 11*i has length n
        for i in xrange(en // 11, max(p // en, en1 // 11), -1):
            if p % i == 0:
                return p * 11
                # return (i * 11, p // i), p * 11



if __name__ == '__main__':

    length = 10
    # print palindrome_product_0(length)
    # print palindrome_product_1(length)
    # print palindrome_product_2(length)
    # print palindrome_product_3(length)
    for i in range(3, 8):
        print i, palindrome_product_4(i)
    
    times = 10

    # t1 = timeit.timeit("palindrome_product_0(3)",
    #                    setup="from __main__ import palindrome_product_0", number=times)/float(times)
    # print '{} ms'.format(10**3*t1)

    # times = 100
    # t2 = timeit.timeit("palindrome_product_1(3)",
    #                    setup="from __main__ import palindrome_product_1", number=times)/float(times)
    # print '{} ms'.format(10**3*t2)

    # times = 1000
    # t3 = timeit.timeit("palindrome_product_2(3)",
    #                    setup="from __main__ import palindrome_product_2", number=times)/float(times)
    # print '{} ms'.format(10**3*t3)

    # times = 1000
    # t4 = timeit.timeit("palindrome_product_3(3)",
    #                    setup="from __main__ import palindrome_product_3", number=times)/float(times)
    # print '{} ms'.format(10**3*t4)

    times = 1
    t5 = timeit.timeit("palindrome_product_4(9)",
                       setup="from __main__ import palindrome_product_4", number=times)/float(times)
    print '{} ms'.format(10**3*t5)