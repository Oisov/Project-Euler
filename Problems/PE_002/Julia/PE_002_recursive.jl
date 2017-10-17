function fib(n)
    if n < 2
        return n
    else
        return fib(n - 1) + fib(n - 2)
    end
end


function PE_002_recursive(limit=4 * 10^6)
    n = total = 0
    while fib(n) < limit
        n += 1
        if fib(n) % 2 == 0
            total += fib(n)
        end
    end
    total
end
