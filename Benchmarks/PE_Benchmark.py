import os
import timeout_decorator
import timeit
import time
import sys
import importlib


LANGUAGES = {"python": "py", "julia": "jl", "java": "class"}


def get_PE_dir(PE):
    return os.path.dirname(os.getcwd()) + '/Problems/' + 'PE_{:0>3}'.format(PE)


def get_languages(PE):
    cwd = get_PE_dir(PE)
    languages = []
    for fname in os.walk(cwd).next()[1]:
        if fname.lower() in LANGUAGES.keys():
            languages.append(fname.lower())
    return languages


def define_function(PE):
    path = get_PE_dir(PE) + '/Python'
    filename = 'PE_{:0>3}'.format(PE)
    sys.path.insert(0, path)
    module = importlib.import_module(filename)
    return getattr(module, filename)


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


