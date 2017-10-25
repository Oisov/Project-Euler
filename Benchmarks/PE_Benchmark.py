import os
import timeout_decorator
import timeit
import time
import sys

LANGUAGES = {"python": "py",
             "julia": "jl",
             "java": "class"
}

def get_PE_dir(PE):
    return os.path.dirname(os.getcwd()) + '/Problems/' + 'PE_{:0>3}'.format(
        PE)


def get_languages(PE):
    cwd = get_PE_dir(PE)
    languages = []
    for fname in os.walk(cwd).next()[1]:
        if fname.lower() in LANGUAGES.keys():
            languages.append(fname.lower())
    return languages
