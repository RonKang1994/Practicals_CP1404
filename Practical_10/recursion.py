"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)
    # 1 + 0 + 1 + 0 + 1 + 0


# TODO: 1. write down what you think the output of this will be,
# Output will be 6
# TODO: 2. use the debugger to step through and see what's actually happening
# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
        do_something(n - 1)

# TODO: 3. write down what you think the output of do_something(4) will be,
# Output = 1
# TODO: 4. use the debugger to step through and see what's actually happening
# do_something(4)

# TODO: 5. fix do_something() so that it works according to the docstring

# Recursion From Scratch 2D pyramid block
def block_pyramid_count(n):
    if n <= 0:
        return 0
    return n + block_pyramid_count(n - 1)


print(block_pyramid_count(6))