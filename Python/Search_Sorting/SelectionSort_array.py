import time 

A = [100,9,25,45,77,13,1,0]


def selectionSort( A ):    

    for i in range(len(A) - 1):
        minIdx = i
        
        for j in range(minIdx+1,len(A )):
        
            if A[j] < A[minIdx]:
                minIdx = j
        
        if i != minIdx:
            A[i], A[minIdx] = A[minIdx], A[i]

#Medir el tiempo de ejecucion
inicio = time.perf_counter()
print( "Array en desorden -->", A )
selectionSort( A ) 
print( "Array en orden    -->", A )
final = time.perf_counter()
print(f"Items sorted in {final - inicio : 0.4f} seconds")
