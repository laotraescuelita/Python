import time 

A = [100,9,25,45,77,13,1,0]

def quickSort(A, start, end):	
	
	if start < end:		
		mid = partition( A, start, end) 
		quickSort( A, start, mid-1)
		quickSort( A, mid+1, end )
	return A 

def partition(A, start, end): 
	idx = start
	pivot = A[idx]

	while start < end: 
		while start < len( A ) and A[start] <= pivot: 
			start += 1 

		while A[end] > pivot: 
			end -= 1

		if start < end:			
			A[start],A[end] = A[end],A[start]			
		
	A[idx],A[end] = A[end],A[idx]			
	
	return end 

#Medir el tiempo de ejecucion
inicio = time.perf_counter()
print( "Array en desorden -->", A )
quickSort( A, 0, len(A)-1) 
print( "Array en orden    -->", A )
final = time.perf_counter()
print(f"Items sorted in {final - inicio : 0.4f} seconds")
 

