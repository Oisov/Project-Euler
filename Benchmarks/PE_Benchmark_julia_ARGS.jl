include("PE_Benchmark_julia.jl")

benchmark_all_julia(parse(Int, ARGS[1]))
