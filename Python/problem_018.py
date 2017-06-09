import string


def strip_string(str):
    all = string.maketrans('', '')
    nodigs = all.translate(all, string.digits)
    return str.translate(all, nodigs)


def pyramid_file(filename):
    file = open(filename, 'r')
    pyramid = list()
    for index, line in enumerate(file):
        if index > 0:
            pyramid.extend([[int(i) for i in line.split()]])
        else:
            pyramid.extend([[int(strip_string(line))]])
    return pyramid


def path_pyramid(pyramid):
    layer = len(pyramid)-1
    pyramid_row_0 = pyramid[layer-1]
    pyramid_row_1 = pyramid[layer]
    chains = []
    for i, num in enumerate(pyramid_row_0):
        left = pyramid_row_1[i]
        right = pyramid_row_1[i+1]
        if left > right:
            chains.append([num, left])
        else:
            chains.append([num, right])
    
    print chains
    print

    for k in range(2, layer):
        temp_chains = []
        for i, num in enumerate(pyramid[layer-k]):
            left = sum(chains[i])
            right = sum(chains[i+1])
            if left > right:
                chain = list(chains[i])
                chain.insert(0, num)
                temp_chains.extend([chain])
            else:
                chain = list(chains[i+1])
                chain.insert(0, num)
                temp_chains.extend([chain])
        chains = temp_chains

        print chains
        print

    max_sum = 0
    for ch in chains:
        ch.insert(0, pyramid[0][0])
    	if sum(ch) > max_sum:
    		sols = ch
    return sols


def print_pyramid(pyramid, solution):
    pyramid_row = len(pyramid)-1
    print "================================================================================"
    for index, row in enumerate(pyramid):
        lin = ""
        for i in row:
            if i == solution[index]:
                lin += str([i])
                lin += "  "
            elif i < 10:
                lin += " "
                lin += str(i)
                lin += "   "
            else:
                lin += str(i)
                lin += "   "
        print lin.center(75)
    print "==============================================================================="
    print "Length of the longest path = " + str(sum(solution))
    print "path = " + str(solution)
    print "==============================================================================="

if __name__ == '__main__':

    pyramid = pyramid_file('018.txt')

    sol = path_pyramid(pyramid)
    print_pyramid(pyramid, sol)
