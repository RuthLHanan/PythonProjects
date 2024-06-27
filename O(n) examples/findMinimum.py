#Find and return minimum element in a list
def find_min(arr):
    minimum = arr[0]
    for element in arr:
        if element < minimum:
            minimum = element
    return minimum

arr = [10, 3, 9, 1, 24]
find = find_min(arr)
print(find)
