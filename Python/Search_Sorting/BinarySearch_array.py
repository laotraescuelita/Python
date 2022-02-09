import time
A = [100,9,25,45,77,13,1,0,12]
ASorted =  sorted(A)
print( ASorted	)

def binarySearch( A, item): 
	i = 0 
	j = len( A ) - 1
	
	while i < j: 
		mid = (i + j ) // 2
		if A[mid] == item: 
			return mid
		elif A[mid] < item: 
			i = mid + 1
			print( i , A[i])
		else: #A[mid] > item
			j = mid - 1
			print( j , A[j])
	return "Item was not found!" 

inicio = time.perf_counter()
print( binarySearch( ASorted, 13) )
final = time.perf_counter()
print(f"Item found in {final - inicio : 0.4f} seconds")
