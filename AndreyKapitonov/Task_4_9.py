"""### Task 4.9

Implement a bunch of functions which receive a changeable number of strings and return next parameters:
1) characters that appear in all strings
2) characters that appear in at least one string
3) characters that appear at least in two strings
4) characters of alphabet, that were not used in any string
Note: use `string.ascii_lowercase` for list of alphabet letters
```python
test_strings = ["hello", "world", "python", ]
print(test_1_1(*strings))
>>> {'o'}
print(test_1_2(*strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*strings))
>>> {'h', 'l', 'o'}
print(test_1_4(*strings))
>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
```
"""


#  Attention! All these functions use module string!!!
import string


# return characters that appear in all strings
def test_1_1(*strings):
    all_strings_char = set()
    for character in string.ascii_lowercase:
        for t_string in test_strings:
            all_strings_char.add(character)
            if t_string.lower().find(character) == -1:
                all_strings_char.remove(character)
                break
    return(all_strings_char)


# return characters that appear in at least one string
def test_1_2(*strings):
    all_strings_char = set()
    for character in string.ascii_lowercase:
        for t_string in test_strings:
            if character in all_strings_char:
                continue
            elif t_string.lower().find(character) != -1:
                all_strings_char.add(character)
    return(all_strings_char)


# return characters that appear at least in two strings
def test_1_3(*strings):
    all_strings_char = set()
    for character in string.ascii_lowercase:
        N = 0 # counter of appearances of a character in different strings
        for t_string in test_strings:
            if character in all_strings_char:
                continue
            elif t_string.lower().find(character) != -1:
                N += 1
                if N == 2:
                    all_strings_char.add(character)
    return(all_strings_char)


# return characters of alphabet, that were not used in any string
def test_1_4(*strings):
    all_strings_char = set()
    for character in string.ascii_lowercase:
        for t_string in test_strings:
            if t_string.lower().find(character) != -1:
                if character in all_strings_char:
                    all_strings_char.remove(character)
                break
            all_strings_char.add(character)
    return(all_strings_char)


# Let's test these four functions
test_strings = ["Hellooooo", "wOrld", "python"]
print('1. characters that appear in all strings:\n', test_1_1(test_strings))
print('2. characters that appear in at least one string:\n', test_1_2(test_strings))
print('3. characters that appear at least in two strings:\n', test_1_3(test_strings))
print('4. characters of alphabet, that were not used in any string:\n', test_1_4(test_strings))

