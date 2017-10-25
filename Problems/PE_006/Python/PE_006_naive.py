#!/usr/bin/env python


def naive(n):
    square_sum = sum(i**2 for i in range(n + 1))
    natural_sum = sum(i for i in range(n + 1))
    return natural_sum**2 - square_sum


if __name__ == "__main__":

    print naive()