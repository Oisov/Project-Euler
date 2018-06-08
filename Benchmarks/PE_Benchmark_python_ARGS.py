import sys
import PE_Benchmark_python

args = len(sys.argv) - 1
if args == 1:
    benchmark_python(sys.argv[1])
elif args == 2:
    benchmark_python(sys.argv[1], sys.argv[2])
