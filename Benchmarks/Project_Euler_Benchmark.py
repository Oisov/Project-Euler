import os, sys

from PE_Benchmark import *
from PE_create_testdata import *
from PE_Benchmark_Plot import *
from PE_markdown import *

def benchmark_project_euler(PE):
    lang = get_languages(PE)
    for language in lang:
        if language == 'julia':
            os.system('julia PE_Benchmark_julia_ARGS.jl {}'.format(PE))
        elif language == 'python':
            os.system('python PE_Benchmark_python_ARGS.py {}'.format(PE))
    create_markdown(PE, True)


if __name__ == "__main__":

    PE = 6
    # create_testdata(PE, 1, 500, step=15)
    # create_testdata(PE, 500, 100000, step=15)
    benchmark_project_euler(PE) #testfile to benchmark data
    benchmark(PE) #benchmark data to plot
    create_markdown(PE, True) #Plot into markdown
