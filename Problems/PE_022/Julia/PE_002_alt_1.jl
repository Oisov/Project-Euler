OFFSET = Int('A')

OFFSET = Int('A') - 1

function namescore(name)
    return sum(Int(letter)-OFFSET for letter in name)
end

function sort_file(filename)
    file = open(filename)
    sort(split(readstring(filename),","))
end


function PE_022_alt_1(filename="../p022_names.txt")
    total = 0
    for (index, name) in enumerate(sort_file(filename))
        total += index*namescore(name[2:end-1])
    end
    total
end

println(PE_022_alt_1())
