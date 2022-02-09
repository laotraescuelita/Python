import time 

A = [100,9,25,45,77,13,1,0]

def mergeSort( A ):
    if len( A ) <= 1:
        return 

    mid = len( A ) // 2
    left = A[:mid]
    right = A[mid:]

    mergeSort( left )
    mergeSort( right )

    mergeSortLists( left, right, A)

def mergeSortLists( l, r, A):
    len_l = len( l )
    len_r = len( r )
    i = j = k = 0 

    while i < len_l and j < len_r: 
        if l[i] <= r[j]:
            A[k] = l[i]
            i += 1 
        else: #l[j] <= r[i]:
            A[k] = r[j]
            j += 1 
        k += 1 

    while i < len_l: 
        A[k] = l[i]
        i += 1 
        k += 1

    while j < len_r: 
        A[k] = r[j]
        j += 1 
        k += 1 

#Medir el tiempo de ejecucion
inicio = time.perf_counter()
print( "Array en desorden -->", A )
mergeSort( A ) 
print( "Array en orden    -->", A )
final = time.perf_counter()
print(f"Items sorted in {final - inicio : 0.4f} seconds")
 

