
import os
import timeout_decorator
import timeit
import time
import sys
import numpy as np
from matplotlib import pyplot as plt
from matplotlib2tikz import save as tikz_save

from PE_Benchmark import LANGUAGES, get_PE_dir, get_languages



def read_test_data(PE, filename):
    path = get_PE_dir(PE) + '/Tests/' + filename
    PE_input, result, labels = list(), list(), list()
    with open(path) as f:
        for line in f:
            line_list = line.strip().split(':')
            PE_input.append(line_list[1])
            result.append(line_list[2])
            labels.append(line_list[0])
    return (PE_input, result, labels)


def is_benchmark_datafile(filename, testname, language):
    if language.lower() in ['all', True]:
        for fileending in LANGUAGES.values():
            filenameending = testname[7:-4] + "." + fileending + ".txt"
            if filenameending in filename:
                return True
        return False

    else:
        filenameending = "." + LANGUAGES[language] + ".txt"
        print filenameending, " : ", filename
        return filenameending in filename


def benchmark_plot(PE, testname, language="all"):

    cwd = get_PE_dir(PE) + '/Benchmarks'
    labels = read_test_data(PE, testname)[2]

    if language in ["all", True]:
        language_name = ""
    else:
        language_name = "- " + language.capitalize()

    for fname in os.listdir(cwd):
        if not is_benchmark_datafile(fname, testname, language):
            continue

        data = np.loadtxt(cwd + '/' + fname)
        X = data[:, 0]
        Y = data[:, 1]
        plt.plot(X, Y, label=fname.replace("_", " ")[12:-4])

    plt.xticks(X, labels)
    plt.legend(loc=2)
    plt.xlabel('Input')
    plt.ylabel('Time')
    plt.title('Project Euler {} - Benchmark {} {}'.format(
        PE, fname[12:14].replace("0", " "), language_name))

    tikz_save('test.tex')
    os.system('pdflatex standalonefile.tex')

    destination = os.path.dirname(os.getcwd()) + '/Raport/Benchmarks'
    new_name = testname[:-4] + '.tex'
    print('===')
    print(os.getcwd()+'/test.tex')
    print(destination+'/'+new_name)
    print('===')
    os.rename(os.getcwd()+'/test.tex', destination+'/'+new_name)

    image_name = testname[:-4]
    if language not in ["all", True]:
        image_name += "_" + language
    image_name += ".png"

    os.system('convert -density 200 standalonefile.pdf -quality 100 ' + image_name)

    destination = get_PE_dir(PE) + '/Images'
    # plt.show()  #or
    os.rename(os.getcwd()+'/' + image_name, destination+'/'+image_name)



def benchmark_plot_all(PE, language="all"):
    language = language.lower()
    cwd = get_PE_dir(PE) + '/Tests'
    for testfile in os.listdir(cwd):
        benchmark_plot(PE, testfile, language)


if __name__ == '__main__':
    print(benchmark_plot_all(2))
