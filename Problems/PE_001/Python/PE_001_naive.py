def PE_001_naive(divisors=[3, 5], stop=100, start=1):
    count = 0
    for num in xrange(start, stop):
        for d in divisors:
            if num % d == 0:
                count += num
                break
    return count


if __name__ == "__main__":

    print(PE_001_naive())
