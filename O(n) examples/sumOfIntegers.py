#List of integers and returns a sum
def sum_elements(arr):
    total = 0
    for element in arr:
        total += element
    return total

arr = [1, 2, 3, 4, 5]
sum = sum_elements(arr)
print(sum)