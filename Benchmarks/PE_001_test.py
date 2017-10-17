import os
import timeout_decorator
import timeit
import time
import sys

# from PE_001 import PE_001


def time_bolean(n, filename, setup):
    @timeout_decorator.timeout(5)
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
        return float('inf')

    middle_n = (max_n + min_n) // 2
    middle_bol = time_bolean(middle_n, filename, setup)

    i = 0
    while (max_n - min_n > 10) and i < 10**5:
        if not middle_bol:
            max_n = middle_n
        else:
            min_n = middle_n

        middle_n = (max_n + min_n) // 2
        middle_bol = time_bolean(middle_n, filename, setup)
        i += 1

    return middle_n


def avg_run_file(filename, setup, number_of_runs=10**5, average_of=5):
    if number_of_runs == 0:
        number_of_runs = max_runs(filename, setup)
        if number_of_runs == float('inf'):
            number_of_runs = 0

    times = [0] * average_of
    for i in range(average_of):
        times[i] = timeit.timeit(filename, setup, number=number_of_runs)
    if average_of > 4:
        times.remove(max(times))
        times.remove(min(times))
    return sum(times) / len(times)


def find_files(PE=1):
    try:
        int(PE)
        PE_str = str(PE)
    except:
        PE_str = PE

    PE_folder = 'PE_' + (3 - len(PE_str)) * '0' + PE_str
    cwd = os.path.dirname(os.getcwd()) + '/Problems/' + PE_folder

    PE_input, result = list(), list()
    with open(cwd + '/tests.txt') as f:
        for line in f:
            line_list = line.strip().split(':')
            PE_input.append(line_list[0])
            result.append(line_list[1])

    file_dir = cwd + '/Python'
    sys.path.insert(0, file_dir)
    for f in os.listdir(file_dir):
        if not f.endswith('.py'):
            continue
        for index, value in enumerate(PE_input):
            file_no_ending = f[:-3]
            filename = file_no_ending + '(' + value + ')'
            setup = 'from {} import {}'.format(file_no_ending, file_no_ending)

            time_taken = avg_run_file(filename, setup, number_of_runs=0)
            print(time_taken, value, file_no_ending)

    # for filename in os.listdir('.'):
    #     if filename.endswith(".asm") or filename.endswith(".py"):
    #         # print(os.path.join('.', filename))
    #         continue
    #     else:
    #         continue


if __name__ == '__main__':
    # a = mytest('001_naive.py')
    # b = mytest('001.py')
    # print('Naive: ', a)
    # print('PE_001: ', b)
    # print(bijection_timer())
    # string = 'PE_001([3,5], 10**4, 1)'
    # print(timeit.timeit(string, setup='from PE_001 import PE_001',number=100))
    # print(PE_001([3, 5], 10, 100))

    print(find_files(2))
