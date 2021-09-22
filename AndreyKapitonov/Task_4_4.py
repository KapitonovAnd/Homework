"""### Task 4.4

Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
which splits the `s` string by indexes specified in `indexes`. Wrong indexes
must be ignored.
Examples:
```python
#>>> split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])
["python", "is", "cool", ",", "isn't", "it?"]

#>>> split_by_index("no luck", [42])
["no luck"]
```"""


def split_by_index(s, indexes):
    indexes = sorted(set([0] + indexes + [len(s)]))

# Indices validation
    i = 0
    while i < len(indexes):
        if indexes[i] > len(s):
            del indexes[i]
        else: i += 1

# New list for splitted words
    splitted = []
    for i in range(0, len(indexes) - 1):
        word = s[indexes[i]:indexes[i+1]]
        splitted.append(word)
    return splitted


# Let's check this gunction:
s_in = "pythoniscool,isn'tit?"
print('input string:', s_in)
indexes_in = [6, 12, 8, 13, 21, 18, 42, 100, 10000000]
print('input indices:', indexes_in)
print('result:', split_by_index(s_in, indexes_in))

