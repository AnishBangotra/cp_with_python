def quickSort(arr):
	if len(arr)<=1:
		return arr
	else:
		pivot = arr.pop()
	lower_items = []
	greater_items = []
	for item in arr:
		if item > pivot: greater_items.append(item)
		else: lower_items.append(item)
	return quickSort(lower_items) + [pivot] + quickSort(greater_items)