"""### Task 1.6

Write a Python program to convert a given tuple of positive integers into an integer. 
Examples:
```
Input: (1, 2, 3, 4)
Output: 1234
```
"""
Input_Tuple = (1, 2, 3, 4)
Output_Integer = 0
Digits = len(Input_Tuple) - 1
for Number in Input_Tuple:
    Output_Integer += Number*10**(Digits - Input_Tuple.index(Number))
print(Output_Integer)