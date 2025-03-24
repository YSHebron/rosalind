def merge_sort(arr) -> list:
    if len(arr) == 1:
        return arr
    median = round(len(arr)/2)
    arr1 = merge_sort(arr[0:median])
    arr2 = merge_sort(arr[median:])
    if arr2[0] < arr1[0]:
        return arr2 + arr1
    else:
        return arr1 + arr2

arr = [5, 2, 3, 8, 7]
print(merge_sort(arr))
    