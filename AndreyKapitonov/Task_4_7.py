"""### Task 4.7

Implement a function `foo(List[int]) -> List[int]` which, given a list of
integers, return a new list such that each element at index `i` of the new list
is the product of all the numbers in the original array except the one at `i`.
Example:
```python
>>> foo([1, 2, 3, 4, 5])
[120, 60, 40, 30, 24]

>>> foo([3, 2, 1])
[2, 3, 6]
```
"""


def foo(List):
    product = 1
    for number in List:
        product *= number
    result = []
    for number in List:
        result += [product//number]
    return(result)


# Let's check this function:
input_list = []
input_str = input('Press Enter to process default list: [1, 2, 3, 4, 5] \n'
                  'or enter your own list of integers:')
if input_str == '':
    input_list = [1, 2, 3, 4, 5]
else:
    input_str = input_str.split()
    input_list = [int(word) for word in input_str]
print('Input list:', input_list)
print('result:', foo(input_list))

