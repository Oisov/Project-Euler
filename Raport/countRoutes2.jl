cache = Dict()

function countRoutes(m, n)

    if n == 0 || m == 0
        return 1
    end

    try
        return cache[(m, n)]
    end
    cache[(m, n)] = countRoutes(m, n - 1) + countRoutes(m - 1, n)
    cache[(n, m)] = cache[(m, n)]
    return cache[(m, n)]
end

println(countRoutes(20, 20))
