"""#### Task 4.8

Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
of tuples containing pairs of elements. Pairs should be formed as in the
example. If there is only one element in the list return `None` instead.
Example:
```python
>>> get_pairs([1, 2, 3, 8, 9])
[(1, 2), (2, 3), (3, 8), (8, 9)]

>>> get_pairs(['need', 'to', 'sleep', 'more'])
[('need', 'to'), ('to', 'sleep'), ('sleep', 'more')]

>>> get_pairs([1])
None
```
"""


def get_pairs(lst):
    N = len(lst) - 1
    if N < 2:
        return None
    else:
        output_list = []
        for i in range(N):
            output_list += [(lst[i], lst[i + 1])]
        return output_list


# Let's check this function:
input_list = [ 1, 2, 3, 8, 9, 'need', 'to', 'sleep', 'more']
print('Input list:', input_list)
print('result:', get_pairs(input_list))

