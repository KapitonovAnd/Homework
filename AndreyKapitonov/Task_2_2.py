'''### Task 1.2

Write a Python program to count the number of characters (character frequency) in a string (ignore case of letters).
Examples:
```
Input: 'Oh, it is python'
Output: {',': 1, ' ': 3, 'o': 2, 'h': 2, 'i': 2, 't': 2, 's': 1, 'p': 1, 'y': 1, 'n': 1}
```'''
String = input("Enter your string or just press Enter to process default string 'Oh, it is python' \n"
               ": " )
if String == '':
    String = 'Oh, it is python'
# Initiate Dictionary to use its Keys for handling every unique Character of String
Dictionary = {}
for Character in String:
    Keys = Dictionary.keys()
    if Character in Keys:
        Dictionary[Character.lower()] += 1
    else:
        Dictionary[Character.lower()] = 1
print(Dictionary)