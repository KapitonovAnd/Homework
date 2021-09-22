"""### Task 4.6

Implement a function `get_shortest_word(s: str) -> str` which returns the
longest word in the given string. The word can contain any symbols except
whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
the string with a same length return the word that occures first.
Example:
```python

>>> get_shortest_word('Python is simple and effective!')
'effective!'

>>> get_shortest_word('Any pythonista like namespaces a lot.')
'pythonista'
```
"""


def get_longest_word(s):
    longest = max(s.split(), key = len)
    return longest


# Let's check this function:
input_str = input('Press Enter to process default string: \'Any pythonista like namespaces a lot.\' \n'
                  'or enter your own string:')
if input_str == '':
    input_str = 'Any pythonista like namespaces a lot.'
print('input string is: "{}"'.format(input_str))
result = get_longest_word(input_str)
print('longest word is: "{0}", its length = {1}'.format(result, len(result)))

