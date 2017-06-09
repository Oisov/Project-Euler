import math 

def sum_first_n_digits(filename, digits = 10):
    return str(sum(int(line) for line in open(filename, 'r')))[0:digits]

def sum_first_n_digits_2(filename, digits = 10):
    total = 0
    with open(filename, "r") as list_of_numbers:
        for number in list_of_numbers:
            total += int(number)
    return str(total)[0:digits]

def sum_first_n_digits_3(filename, digits = 10):
    # This is wrong!
    total = 0
    with open(filename, "r") as list_of_numbers:
        for number in list_of_numbers:
            total += int(number[0:digits+1])
    return str(total)[0:digits]

def first_n_digits(number, digits):
    total_digits = int(math.log(number, 10)+1)
    unsignificant = 10**(total_digits-digits)
    return (number - number%unsignificant)/unsignificant

if __name__ == '__main__':

    print sum_first_n_digits('013.txt')
    print sum_first_n_digits_2('013.txt')
    print sum_first_n_digits_3('013.txt')
    # print first_n_digits(5537376230390876637302048746832985971773659831892672, 10)
    Dette er hvordan det føles å skrive på hverdens beste tastaturx