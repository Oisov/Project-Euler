
from PE_Benchmark import LANGUAGES, get_PE_dir, get_languages

from PE_create_testdata import *
from PE_Benchmark_Plot import *
from PE_markdown import *


print(5)

PE = 6
os.system('julia jul_benchmark.jl {}'.format(PE))
