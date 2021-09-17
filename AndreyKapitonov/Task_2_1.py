'''### Task 1.1

Write a Python program to calculate the length of a string without using the `len` function.'''

Input_String = input('Enter your string: ')
Counter = 0
for Character in Input_String:
    Counter += 1
print('{0} characters in string "{1}"'.format(Counter, Input_String))