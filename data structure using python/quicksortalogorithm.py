# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot


# Function to find the partition position
def partition(a, low, high):

	# choose the rightmost element as pivot
	pivot = a[low]

	# pointer for greater element
	i = low
	j=high
	while(i<j):
	   while(i<=high and a[i]<=pivot):
	        i=i+1
	   while(a[j]>pivot):
	       j=j-1
	   if(i<j):
	       a[i],a[j]=a[j],temp
	a[low],a[j]=a[j],a[low]
	return j
	       

	# traverse through all elements
	# compare each element with pivot
	

# function to perform quicksort


def quickSort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quickSort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quickSort(array, pi + 1, high)


data = [1, 7, 4, 1, 10, 9, -2]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
