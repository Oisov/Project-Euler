from collections import defaultdict

LIMIT = 10**6
collatz_len = defaultdict(int)


def collatz_step(num):
	return num // 2 if num%2 == 0 else 3*num + 1


def collatz_sequence_length(num):
	length = 1
	lst_collatz = [num]
	while num != 1:
		num = collatz_step(num)
		lst_collatz.append(num)
		length += 1
		if collatz_len[num] != 0:
			length += -1 + collatz_len[num]
			break
	for i, item in enumerate(lst_collatz):
		collatz_len[item] = length - i
	return length


def collatz_longest_sequence(limit=LIMIT):
	longest_sequence = 1
	start_num = 1
	for num in xrange(limit-1, limit/2, -2):
		if collatz_len[num] != 0:
			continue
		length_sequence = collatz_sequence_length(num)
		if length_sequence > longest_sequence:
			longest_sequence = length_sequence
			start_num = num
	return (start_num, longest_sequence)


if __name__ == '__main__':
	import timeit
	startnum, length = collatz_longest_sequence(28)
	print startnum, length
	times = 10
	t1 = timeit.timeit("collatz_longest_sequence()", setup="from __main__ import collatz_longest_sequence", number = times)
	print "{} ms".format(t1/float(times))
	# print PE()