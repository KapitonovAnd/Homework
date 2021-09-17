"""### Task 1.6.a

Write a program which makes a pretty print of a part of the multiplication table.
Examples:
```
Input:
a = 2
b = 4
c = 3
d = 7

Output:
	3	4	5	6	7	
2	6	8	10	12	14	
3	9	12	15	18	21	
4	12	16	20	24	28
```
"""
a = 2; b = 4
c = 3; d = 7
print("{}\t".format(''), end='')
for Row in range(c, d + 1):
    print("{}\t".format(Row), end='')
print()
for Line in range(a, b + 1):
    print('{}\t'.format(Line), end = '')
    for Row in  range(c, d + 1):
          print('{}\t'.format(Line*Row), end = '')
    print()
# Use of '{: <Number_of_Spaces}'instead of '{}\t'  could help stabilize output table at larger b and d.