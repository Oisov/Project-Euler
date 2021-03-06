def is_palindrome(number):
    string = str(number)
    return string == string[::-1]


def PE_004_early_exit(length = 3):
    palindrome_max = 0
    lower = 10**(length - 1) + 1
    higher = 10**length
    for i in range(higher, lower, -1):
        if i * i <= palindrome_max:
            break
        for j in range(i, lower, -1):
            if is_palindrome(str(i * j)):
                palindrome = i * j
                if palindrome > palindrome_max:
                    palindrome_max = palindrome
                    break
    return palindrome_max
