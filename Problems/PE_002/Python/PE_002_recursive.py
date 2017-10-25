def PE_002_recursive(limit=4 * 10**6):
    fib_ = dict()

    def fib(n):
        try:
            return fib_[n]
        except:
            pass

        if n < 2:
            return n
        else:
            fib_[n] = fib(n - 1) + fib(n - 2)
            return fib_[n]

    n = total = 0
    while fib(n) < limit:
        n += 1
        if fib(n) % 2 == 0:
            total += fib(n)
    return total


if __name__ == "__main__":

    print(PE_002_recursive())
