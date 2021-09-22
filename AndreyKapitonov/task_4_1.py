def replacing_quotations(string):
    """### Task 4.1

    Implement a function which receives a string and replaces all `"` symbols with `'` and vise versa."""
    modified_string = string.translate({ord('"'): '\'', ord('\''): '"'})
    return modified_string


# Let's check this function:
initial_string = input("Enter your string or just press Enter to process default string \n"
"\'Implement\' \"a\" \'function\' \"which\" \'receives\' \"a\" \'string\' \"and\" \'replaces\' \"all\" `\"` \'symbols\' \"with\" `\'` \'and\' \"vise\" \'versa\'. \n"
               ": " )
if initial_string == '':
    initial_string = '\'Implement\' \"a\" \'function\' \"which\" \'receives\' \"a\" \'string\' \
\"and\" \'replaces\' \"all\" `\"` \'symbols\' \"with\" `\'` \'and\' \"vise\" \'versa\'.'
print(initial_string)
modified_string = replacing_quotations(initial_string)
print(modified_string)

