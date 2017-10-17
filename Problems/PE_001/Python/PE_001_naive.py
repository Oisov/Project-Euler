import sys
import ast

def PE_001_naive(divisors=[3, 5], stop=100, start=1):
    count = 0
    for num in xrange(start, stop):
        for d in divisors:
            if num % d == 0:
                count += num
                break
    return count


if __name__ == "__main__":

    if len(sys.argv) == 4:
        PE_001_naive(ast.literal_eval(sys.argv[1]),
                     int(sys.argv[2]),
                     int(sys.argv[3]))
    else:
        PE_001_naive()
