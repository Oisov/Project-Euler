using Primes


function number_of_digits(number)
    Int(floor(log(10, number)+1))
end


function number_2_palindrome(number)
    str_num = string(number)
    parse(Int, str_num * reverse(str_num))
end


function PE_004(palindrome_length = 3, reverse_range = true)
    max_num , min_num = 10^(palindrome_length)-1, 10^(palindrome_length-1)
    range = reverse_range?(max_num:-1:min_num):(min_num:max_num)
    for number in range

        palindrome = number_2_palindrome(number)
        smaller_palindrome = div(palindrome, 11)
        if isprime(smaller_palindrome)
            continue
        end

        smallest_factor = div(11*smaller_palindrome, 10^(palindrome_length))
        for factor_1 = (10^(palindrome_length)-1):-1:(smallest_factor)
            if smaller_palindrome % factor_1 == 0
                factor_2 = div(smaller_palindrome, factor_1)
                if number_of_digits(11*factor_2) == palindrome_length
                    return palindrome
                end
            end
        end
    end
end
