import os, importlib, sys

from PE_Benchmark import get_PE_dir, define_function

def get_next_testnumber(PE, path):
    PE_name = 'PE_{:0>3}'.format(PE)
    max_number = 0
    for filename in os.listdir(path):
        number = int(filename[12:14])
        if number > max_number:
            max_number = number
    return max_number+1


def create_testdata(PE, minimum, maximum, step=15):
    fun = define_function(PE)
    steplength = max((maximum - minimum) // step, 1)
    if steplength == 1:
        step = maximum - minimum

    current = minimum - steplength

    step_pad = len(str(maximum))
    ans_pad = len(str(fun(maximum)))

    path = get_PE_dir(PE)
    test_path = path + '/Tests'
    if os.path.exists(test_path):
        nxt_num = get_next_testnumber(PE, test_path)
    else:
        nxt_num = 1
        os.makedirs(test_path)

    file_2_write = '{}/Tests/PE_{:0>3}_test_{:0>2}.txt'.format(path,
                                                               PE,
                                                               nxt_num)

    fil = open(file_2_write, "w")

    for i in range(step + 1):
        current += steplength
        line= '{}: {number:{width}d} : {number_2:{width_2}d}'.format(
            i+1, width=step_pad, number=current, width_2=ans_pad,
        number_2=fun(current))
        print(line)
        fil.write(line+"\n")
    fil.close()
