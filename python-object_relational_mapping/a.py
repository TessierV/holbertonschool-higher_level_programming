#!/usr/bin/python3
def perfect_number(numbers):
    higher = -1
    for num in numbers:
        if numbers.count(num) == num and num > higher:
            higher = num
    return higher

numbers1 = [2, 2, 3, 4]
largest1 = perfect_number(numbers1)
print(largest1)  

numbers2 = [2, 2, 2, 3, 3]
largest2 = perfect_number(numbers2)
print(largest2)