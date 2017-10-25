import os
import timeout_decorator
import timeit
import time
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib2tikz import save as tikz_save

# from PE_001 import PE_001


def time_bolean(n, filename, setup):
    @timeout_decorator.timeout(1)
    def timity(n):

        timespent = timeit.timeit(filename, setup, number=n)
        return True

    try:
        return timity(n)
    except:
        return False


def max_runs(filename, setup, max_n=10**5, min_n=1):

    max_bol = time_bolean(max_n, filename, setup)
    min_bol = time_bolean(min_n, filename, setup)

    if max_bol:
        return max_n
    elif not min_bol:
        return 0

    while min_bol:
        min_n *= 2
        min_bol = time_bolean(min_n, filename, setup)
    return min_n


def avg_run_file(filename, setup, number_of_runs=10**5, average_of=5):
    if number_of_runs == 0:
        number_of_runs = max_runs(filename, setup)
        if number_of_runs == 0: return 0

    times = [0] * average_of
    for i in range(average_of):
        times[i] = timeit.timeit(filename, setup, number=number_of_runs)
    if average_of > 4:
        times.remove(max(times))
        times.remove(min(times))
    return sum(times) / (len(times) * number_of_runs)


def get_PE_dir(PE):
    return os.path.dirname(os.getcwd()) + '/Problems/' + 'PE_{:0>3}'.format(PE)


def read_test_data(PE, filename):
    path = get_PE_dir(PE) + '/Tests/' + filename
    PE_input, result, labels = list(), list(), list()
    with open(path) as f:
        for line in f:
            line_list = line.strip().split(':')
            PE_input.append(line_list[1])
            result.append(line_list[2])
            if not line_list[0]:
                continue
            labels.append(line_list[0])
    return (PE_input, result, labels)


def benchmark_python_testfile(PE, testfile):

    print(PE, testfile)

    cwd = get_PE_dir(PE)
    PE_input = read_test_data(PE, testfile)[0]

    file_dir = cwd + '/Python'
    sys.path.insert(0, file_dir)
    for f in os.listdir(file_dir):
        if not f.endswith('.py'):
            continue

        file_no_ending = f[:-3]
        print(f)
        filename_2_write = cwd + '/Benchmarks/' + testfile[:-4] + f[6:] + '.txt'
        file = open(filename_2_write, "w")
        for index, value in enumerate(PE_input):
            filename = file_no_ending + '(' + value + ')'
            setup = 'from {} import {}'.format(file_no_ending, file_no_ending)

            time_taken = avg_run_file(filename, setup, number_of_runs=0)
            print(time_taken)
            if time_taken == 0:
                break

            file.write(str(index) + " " + str(time_taken) + "\n")
            print(time_taken, value, file_no_ending)
        file.close()
    # for filename in os.listdir('.'):
    #     if filename.endswith(".asm") or filename.endswith(".py"):
    #         # print(os.path.join('.', filename))
    #         continue
    #     else:
    #         continue


def benchmark_python(PE, testfile = 'all'):
    PE_dir = get_PE_dir(PE)
    cwd = PE_dir + '/Tests/'

    testfile_lst = []
    if testfile == 'all':
        for f in os.listdir(cwd):
            testfile_lst.append(f)
    else:
        testfile_lst.append(testfile)

    if not testfile:
        return

    if not os.path.exists(PE_dir + '/Benchmarks'):
        os.makedirs(PE_dir + '/Benchmarks')

    for testfil in testfile_lst:
        benchmark_python_testfile(PE, testfil)


if __name__ == '__main__':
    # a = mytest('001_naive.py')
    # b = mytest('001.py')
    # print('Naive: ', a)
    # print('PE_001: ', b)
    # print(bijection_timer())
    # string = 'PE_001([3,5], 10**4, 1)'
    # print(timeit.timeit(string, setup='from PE_001 import PE_001',number=100))
    # print(PE_001([3, 5], 10, 100))

    # print(find_files(1))
    # benchmark_plot(PE=1)
    print(benchmark_python(6))
