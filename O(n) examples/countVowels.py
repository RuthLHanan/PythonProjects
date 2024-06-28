#Take a list and return number of vowels
def count_vowels(arr):
    vowels = ["a", "e", "i", "o", "u"]
    total = 0
    for word in arr:
        for element in word:
            if element in vowels:
                total +=1
    return total

arr = ["apple", "banana"]
vowel_total = count_vowels(arr)
print(vowel_total)