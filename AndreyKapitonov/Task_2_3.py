""""### Task 1.3

Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form.
Examples:
```
Input: ['red', 'white', 'black', 'red', 'green', 'black']
Output: ['black', 'green', 'red', 'white', 'red']
```
"""
Sequence = input("Enter your comma separated sequence of words or just press Enter \n"
                 "to process default sequence 'red', 'white', 'black', 'red', 'green', 'black' \n"
                 ": " )
# Attention! Typing whitespace after comma leads to duplication of the first input word in the output.
if Sequence == '':
    List = ['red', 'white', 'black', 'red', 'green', 'black']
else:
    List = Sequence.split(',')
print(sorted(set(List)))