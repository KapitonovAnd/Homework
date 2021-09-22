def palindrome(string):
    """### Task 4.2

    Write a function that check whether a string is a palindrome or not. Usage of
    any reversing functions is prohibited. To check your implementation you can use
    strings from [here](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes)."""
# Transform Capitalised characters into lower case
    modified_string = string.lower()
# Remove all characters except for alphabetic or numeric
    for character in modified_string:
        if character.isalnum():
            continue
        else:
            modified_string = modified_string.replace(character, '')
    return modified_string == modified_string[::-1]


# Let's check this function:
initial_string = input("Enter your string or just press Enter to process default string \n"
                     "\'А роза упала на лапу Азора.\': ")
if initial_string == '':
        initial_string = 'А роза упала на лапу Азора.'
result = palindrome(initial_string)
print('{0}, your string is{1} palindrome'.format(result, ' not'*(not result)))

