import time 

A = [100,9,25,45,77,13,1,0]

def shellSort( A ):    
    mid = len( A ) //2

    while mid > 0:
        for i in range(mid, len(A)):
            pivot = A[i]
            j = i
            while j >= mid and A[j-mid] > pivot:
                A[j] = A[j-mid]
                j -= mid
            A[j] = pivot
        mid = mid // 2

def foo( A ):    
    mid = len( A ) // 2
    mid = 3
    for i in range(mid, len( A ) ):
        pivot = A[i]
        j = i
        while j >= mid and A[j-mid] > pivot:
            A[j] = A[j-mid]
            j -= mid
        A[j] = pivot

#Medir el tiempo de ejecucion
inicio = time.perf_counter()
print( "Array en desorden -->", A )
shellSort( A ) 
print( "Array en orden    -->", A )
final = time.perf_counter()
print(f"Items sorted in {final - inicio : 0.4f} seconds")
