'''a = [12, 5, 7]
l = len(a)
arr = []
'''
arr=[]
while True:
    num = int(input("Enter number (0 to stop): "))
    
    if num == 0:
        break
    
    arr.append(num)
    
l=len(arr)
'''
for i in range(l):
    min_index = i
    
    for j in range(i + 1, l):
        if arr[j] < arr[min_index]:
            min_index = j

    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

print(arr)
'''
#bubble sort
'''
for i in range(l):
    for j in range(0, l - i - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print(arr)

'''
#insertion sort
'''
for i in range(1, l):
    temp = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > temp:
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = temp

print(arr)
'''

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for i in range(1, len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


a = quick_sort(arr)
print(a)
