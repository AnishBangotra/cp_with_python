def permutate(s, space):
	if len(s)==0:
		print(space, end=" ")
	for i in range(len(s)):
		char = s[i]
		left_sub = s[0:i]
		right_sub = s[i+1:]
		res = left_sub + right_sub
		permutate(res, space + char)
		
space = ''
s = input('string')
permutate(s, space)