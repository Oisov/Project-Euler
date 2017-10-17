# include("/home/oisov/Programming/Project-Euler/Problems/PE_002/Julia/PE_002.jl")

using BenchmarkTools

function get_file_path(PE=1)
    current_folder = pwd()
    PE_folder = "/PE_" * lpad(string(PE),3,"0")
    dirname(pwd()) * "/Problems" * PE_folder * "/Julia"
end


function include_files(PE_dir)
    for filename in readdir(PE_dir)
        filepath = PE_dir * "/" * filename
        @everywhere include($filepath)
    end
end


function benchmark_files(PE_dir)
    for filename in readdir(PE_dir)
        f = getfield(Main, Symbol(filename[1:end-3]))
        a = @elapsed f()
        println(filename, " , ", a)
    end
end

PE = 2
PE_dir = get_file_path(PE)
include_files(PE_dir)
benchmark_files(PE_dir)
