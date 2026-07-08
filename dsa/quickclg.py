swap_count = 0

def quicksort(a, l, r):
    global swap_count
    if l >= r:
        return

    p = l
    left = l + 1
    right = r

    while True:
        while a[p] <= a[right] and right >= left:
            right -= 1
        if a[p] > a[right]:
            a[p], a[right] = a[right], a[p]
            p = right
            right -= 1
            swap_count += 1
        if right < left:
            break

        while a[p] >= a[left] and right >= left:
            left += 1
        if a[p] < a[left]:
            a[p], a[left] = a[left], a[p]
            p = left
            left += 1
            swap_count += 1
        if right < left:
            break

    quicksort(a, l, p - 1)
    quicksort(a, p + 1, r)

arr = []
while True:
    num = input("Enter number (X to stop): ")
    if num == 'X':
        break
    arr.append(int(num)) 

print("Original array:", arr)
quicksort(arr, 0, len(arr) - 1)
print("Sorted array: ", arr)
print("Total swaps:", swap_count)
