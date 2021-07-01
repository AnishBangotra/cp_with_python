#Bubble Sort python

def BBL(arr):
	for i in range(len(arr)-1,0,-1):
		for j in range(i):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1], arr[j]

arr = [5,3,8,6,7,2]
BBL(arr)
print(arr)
