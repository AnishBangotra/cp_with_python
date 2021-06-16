def maxSubArraySum(a, size):
	max_ending = 0
	max_so_far = 0
	for i in range(size):
		max_ending = max_ending + a[i]
		if max_ending < 0: max_ending = 0
		if max_so_far < max_ending: max_so_far = max_ending
	return max_so_far

maxSubArraySum(array, len(array))
