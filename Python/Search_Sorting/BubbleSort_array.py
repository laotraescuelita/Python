import time

A = [100,9,25,45,77,13,1,0]

def bubbleSort( A ):
	print( "Array en desorden -->", A )
	for i in range( len(A)-1 ):
		for j in range( (len(A)-1) - i):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
	print( "Array in orden -->", A )

#Medir el tiempo de ejecucion
inicio = time.perf_counter()

bubbleSort( A )

final = time.perf_counter()
print(f"Items sorted in {final - inicio : 0.4f} seconds")


