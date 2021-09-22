"""#### T## Task 4.10
"
Implement a function that takes a number as an argument and returns a dictionary,
where the key is a number and the value is the square of that number.
```python
print(generate_squares(5))
>>> {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
"""


def generate_squares(N):
    output_dict = {i: i * i for i in range(1, N + 1)}
    return(output_dict)


# Let's check this function:
N_in = int(input('Enter an integer number:'))
print('Input number =', N_in)
print(generate_squares(N_in))

