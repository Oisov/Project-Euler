import os
import timeout_decorator
import timeit
import time


def mytest(filename):
    i = 0
    total_time = 0
    file_2_time = 'python ' + filename + ' [3,5,8,19] 100000000 1'
    start_time = time.time()  # remember when we started
    while (time.time() - start_time) < 1:
        start = timeit.default_timer()
        os.system(file_2_time)
        stop = timeit.default_timer()
        total_time += stop - start
        i += 1
    print(i)
    return total_time


def timity(n):
    @timeout_decorator.timeout(1)
    def timity_temp(n):

        timespent = timeit.timeit(
            'PE_001([3,5,7], 10**4, 1)',
            setup='from PE_001 import PE_001',
            number=n)

        return timespent

    try:
        return timity_temp(n)
    except:
        return -1


def bijection_timer():
    max_n = 10**5
    min_n = 1

    time_max_n = timity(max_n)
    time_min_n = timity(min_n)

    if time_max_n > -1:
        return time_max_n
    elif time_min_n == -1:
        return float('inf')

    middle_n = (max_n + min_n) // 2
    time_middle_n = timity(middle_n)

    i = 0
    while (max_n - min_n > 10) and i < 10**5:
        if time_middle_n == -1:
            max_n = middle_n
        else:
            min_n = middle_n

        middle_n = (max_n + min_n) // 2
        time_middle_n = timity(middle_n)
        i += 1

    print(middle_n)
    return timeit.timeit(
        'PE_001([3,5,7], 10**4, 1)',
        setup='from PE_001 import PE_001',
        number=middle_n)


if __name__ == '__main__':
    # a = mytest('001_naive.py')
    # b = mytest('001.py')
    # print('Naive: ', a)
    # print('PE_001: ', b)
    print(bijection_timer())
