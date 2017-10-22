function PE_015_iterative(n=20, m=20)
    rows, columns = n+1, m+1
    grid = zeros(BigInt, rows, columns)

    for row = 1:rows
        grid[row, 1] = 1
    end

    for column = 1:columns
        grid[1, column] = 1
    end

    for i = 2:rows
        for j = 2:columns
            grid[i, j] = grid[i-1, j] + grid[i, j-1]
        end
    end

    grid[rows, columns]
end
