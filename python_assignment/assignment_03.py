# Say you have a list value like this:
# spam = ['apples', 'bananas', 'tofu', 'cats']

# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma
# and a space, with and inserted before the last item.

# For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'. But your
# function should be able to work with any list value passed to it.

def eggs(l1):
    for i in range(len(l1)):
        print(l1[i] + ', ', end="")
        if l1[i] == l1[-2]:
            print('and ' + l1[-1], end="")
            break


spam = ['apples', 'bananas', 'tofu', 'cats']
eggs(spam)
