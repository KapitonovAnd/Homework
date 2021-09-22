"""### Task 4.5

Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
of a given integer's digits.
Example:
```python
>>> get_digits(87178291199)
(8, 7, 1, 7, 8, 2, 9, 1, 1, 9, 9)
```
"""


def get_digits(int_number):
    list_out = []
    while int_number > 0:
        list_out += [(int_number % 10),]
        int_number //= 10
    return(tuple(reversed(list_out)))


#Let's check this function:
input_str = input('Press Enter to process default number: 87178291199 or enter your own number:')
if input_str == '':
    input_number = 87178291199
else:
    input_number = int(input_str)
print('input number =', input_number)
result = get_digits(input_number)
print('resulting tuple:', result)

