using BenchmarkTools

function get_PE_dir(PE=1)
    PE_folder = "/PE_" * lpad(string(PE), 3 ,"0")
    dirname(pwd()) * "/Problems" * PE_folder
end


function include_files(PE_dir)
    for filename in readdir(PE_dir)
        filepath = PE_dir * "/" * filename
        @everywhere include($filepath)
    end
end


function read_test_data(PE, filename)

    path = get_PE_dir(PE) * "/Tests/" * filename
    PE_input, result, labels = [], [], []


    open(path) do f
        for (index, line) in enumerate(eachline(f))

            line_list = split(strip(line), ":")

            # Some care is neeeded for PE_input, multiple arguments is
            # split by , this line maps/parses those to a list of Int64/BigInt
            try
                push!(PE_input, map(parse, split(line_list[2],",")))
            catch
                push!(PE_input, map(x->parse(BigInt,x), split(line_list[2],",")))
            end
            push!(result, parse(BigInt, line_list[3]))
            push!(labels, line_list[1])
        end
    end

    return (PE_input, result, labels)
end


function benchmark_julia_testfile(PE, testfile)
    PE_dir = get_PE_dir(PE)
    PE_dir_julia = PE_dir * "/Julia"
    PE_input, results, labels = read_test_data(PE, testfile)

    include_files(PE_dir_julia)

    for filename in readdir(PE_dir_julia)

        if !endswith(filename, "jl")
            continue
        end

        filename_without_ending = Symbol(filename[1:end-3])
        f = getfield(Main, Symbol(filename_without_ending))


        filename_2_write = PE_dir * "/Benchmarks/" * testfile[1:end-4] * filename[7:end] * ".txt"

        open(filename_2_write, "w") do file
            for (index, input) in enumerate(PE_input)
                println(index, ", ", input)
                write(file, string(index-1) * " " * string(@belapsed $f($input...)) * "\n")
            end
        end

    end
end


function benchmark_all_julia(PE)
    for testfile in readdir(get_PE_dir(PE) * "/Tests")
        benchmark_julia_testfile(PE, testfile)
    end
end

PE = 4
filename = "PE_004_test_01.txt"
benchmark_julia_testfile(PE, filename)
