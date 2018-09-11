# /usr/bin/env python

"""
refactoring code from lab 4.4.1
create list of odd number from foo
"""

foo = [1, 2, 3, 4, 5]

# use list comprehension
print([a for a in foo if a % 2])

# use filter() with lambda
print(list(filter(lambda x: x % 2, foo)))
