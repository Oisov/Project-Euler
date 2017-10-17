    using Combinatorics

function remove_non_coprime(divisors)
    new_divisors = []
    divisors = sort(unique(divisors))
    for divisor in divisors
        index = 1
        is_divisible = false
        len_divisors = length(new_divisors)

        while index < len_divisors
            if mod(divisor, divisors[index]) == 0
                is_divisible = true
                break
            else
                index += 1
            end
        end

        if !is_divisible
            push!(new_divisors, divisor)
        end
    end
    return new_divisors
end


function sum_divisible_by_k(k, start, stop)
    sum_start = div(start, k)
    sum_stop = div(stop - 1, k)
    return div(k*(sum_stop+sum_start)*(sum_stop-sum_start+1),2)
end


function PE_001(div = [3, 5], stop = 10^3, start=1)

    divisors = remove_non_coprime(div)
    total = 0

    sign = 1
    for n in 1:length(divisors)
        for permutation in combinations(divisors, n)
            product = lcm(permutation)
            total += sign*sum_divisible_by_k(product, start, stop)
        end
        sign *= -1
    end
    return total
end

println(PE_001([2,3,5,7], 10^6))
