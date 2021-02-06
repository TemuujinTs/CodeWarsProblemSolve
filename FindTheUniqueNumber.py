def find_uniq(arr):
    arr.sort() 
    if arr[-1] > arr[-2]:
        return arr[-1] 
    return arr[0]
print(find_uniq([ 1, 2, 2, 2, 2 ]))