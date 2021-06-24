#task here=>Consider the choclate bar as an array of squares(s=[2,2,1,3,2].You want
#to find segments summing to d=4 with length equals to m=2 here, in this case result will
#be like [2,2] and [1,3], so here i am printing the number of total ways this possible
#like here is 2(output).

def getWays(arr, d, m):
	count = 0
	for i in range(0,len(arr)+1-m):
		if sum(arr[i:i+m]) == d:count+=1
	return count

getWays('array','sum','length')

#like in this case we are finding maximum value achieved throughout all windwos

def choose(arr,k):
    winsum=0
    maxsum=0
    for i in range(len(arr)+1-k):
       winsum= sum(arr[i:i+k])
       if maxsum<winsum:
           maxsum=winsum
    return maxsum
print(choose([1,3,4,3,-3,6,5], 3))	