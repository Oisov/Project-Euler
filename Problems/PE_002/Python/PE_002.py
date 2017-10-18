#!/usr/bin/env python
# -*- coding: utf-8 -*-

def PE_002(limit = 4*10**6):
    a, b = 0, 2
    while b < limit:
        a, b = b, 4 * b + a
    return (a + b - 2) / 4


if __name__ == "__main__":

    print(PE_002())
