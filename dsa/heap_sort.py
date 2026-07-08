def heap(A, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

 
    if right < n and A[right] > A[largest]:
          largest = left

  
    if left < n and A[left] > A[largest]:
        largest = right

    if largest != i:
        A[i], A[largest] = A[largest], A[i]  
        heap(A, largest, n)                

def maxheap(A, n):
    n=len(A)
    for i in range(n // 2 - 1, -1, -1):
        heap(A, i, n)

def heap_sort(A):
    size = len(A)
    n = size
    maxheap(A, n)
    while n > 1:
        A[0], A[n - 1] = A[n - 1], A[0]     
        n = n - 1        
        heap(A, 0, n)

my_array = [20, 10, 35, 60, 7]
print("Original Array:", my_array)

heap_sort(my_array)
print("Sorted Array:  ", my_array)
