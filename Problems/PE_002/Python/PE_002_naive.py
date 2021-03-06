def PE_002_naive(limit=4 * 10**6, F_1=1, F_2=2):
    total = 0
    while F_2 < limit:
        if F_2 % 2 == 0:
            total += F_2
        F_1, F_2 = F_2, F_1 + F_2
    return total


if __name__ == "__main__":

    print(PE_002_naive())
