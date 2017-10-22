function PE_015(grid=[20, 20])
    binomial(BigInt(grid[1] + grid[2]), BigInt(grid[2]))
end

# println(PE_015([500, 500]))

for i =10:10:100
    println(i, " , ", PE_015([i, i]))
end
