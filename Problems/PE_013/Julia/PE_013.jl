function first_n_digits(num, digits = 10)
    BigInt(parse(Float64, string(BigInt(num))[1:digits]))
end

function PE_013(path="../PE_013_input.txt")
    total = 0
    f = open(path)
    for line in readlines(f)
        total += parse(Float64, line)
    end
    first_n_digits(total)
end
