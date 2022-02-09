import time 

A = [100,9,25,45,77,13,1,0]

def insertionSort( A ): 
	for i in range( 1, len(A)):
		key = A[i]		
		j = i - 1 
		while j >= 0 and key < A[j]: 
			A[j+1] = A[j]
			j -= 1 
		A[j+1] = key

#Medir el tiempo de ejecucion
inicio = time.perf_counter()
print( "Array en desorden -->", A )
insertionSort( A ) 
print( "Array en orden    -->", A )
final = time.perf_counter()
print(f"Items sorted in {final - inicio : 0.4f} seconds")
 

