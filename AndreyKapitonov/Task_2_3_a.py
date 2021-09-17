""""#### Task 1.3.a

Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.
Examples:
```
Input: 60
Output: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
```
"""
Number = int(input("Enter your integer nubber: "))
if Number < 0:
    Number = - Number
Divisors = [1, ]
for i in range (2, Number+1):
    if Number % i == 0:
        Divisors.append(i)
print('Divisors of your number are: ', Divisors)