def splitter(string):
    """### Task 4.3

    Implement a function which works the same as `str.split` method
    (without using `str.split` itself, ofcourse)."""
    my_separators = (' ', '\t')
    splitted_string = []
    word = ''
    for character in (string + ' '):
        if character not in my_separators:
            word += character
        elif word == '': continue
        else:
            splitted_string.append(word)
            word = ''
    return splitted_string


# Let's check this function
initial_string = input('Enter your string or just press Enter to process default string:')
if initial_string == '':
        initial_string = """###    Task 4.3        Implement a function which works the same as `str.split` method (without using `str.split` itself, ofcourse)."""
print(initial_string)
result = splitter(initial_string)
print(result)

