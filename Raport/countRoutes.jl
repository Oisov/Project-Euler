function countRoutes(m, n)
    if n==0 || m==0
        return 1
    end
    return countRoutes(m, n - 1) + countRoutes(m - 1, n)
end
