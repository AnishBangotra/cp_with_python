def checkSubsequence(S, string):
	s=[]
	# s as a stack
	for i in range(len(string)):
		s.append(targetString[i])
	for i in range(len(S)-1,-1,-1):
		if len(s)==0:return True
		if S[i]==s[-1]:s.pop()
	if len(s)==0:return('YES')
	else:return('NO')

checkSubsequence('mainString','StringToCheck')