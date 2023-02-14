######################################################################
# Author: Dr. Patrick Shepherd      TODO: Change this to your names
# Username: shepherdp               TODO: Change this to your usernames
#
# Assignment: T5: Buggy Fruit
# Purpose: A program to practice debugging on
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Jan Pearce
#
# Modified from: http://inventwithpython.com/chapter7.html
# for debugging practice
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import random


def squareroot(x):
    """
    Calculates the square root of a number
    :param x: a number to take the square root of
    :return: the square root of x
    """
    answer = x ** 1 / 2
    return answer

def squared(x):
    """
    Calculates the square of a number
    :param x: a number to square
    :return: the square of x
    """
    answer = x ** 2

    # I round the answer to 5 decimal places to avoid any representation errors so
    # that I can reliably compare answers between different methods of calculating
    # the same thing.
    answer = round(answer, 5)
    return answer

def hypoteneuse(a, b):
    """
    Calculates the hypotenuse length on a triangle with other side lengths a and b
    :param a: the length of one side of the triangle
    :param b: the length of another side of the triangle
    :return: the length of the hypotenuse connecting the two sides a and b
    """
    val = 0
    val = val + squared(a)
    val = val + squared(b)
    val = squareroot(val)

    return val

    # Note that this function could also have been written in a single line:
    # return squareroot(squared(a) + squared(b))

    # Breaking it down into individual pieces as we did above can help make
    # one-line solutions clearer to put together!

def main():
    """
    Calculates the sum of two random numbers, compares it to a random sum. Should be correct 25% of the time
    :return: None
    """

    print('Welcome to exploring the debugger!!!')
    print('There is a bug lurking somewhere deep in the darkest reaches of the code above.')

    # Notice how I put a little space between lines with the \n below?
    print('It is your job to hunt it down! (NOT fix it, just find it!)\n')

    number1 = random.randint(1, 5)
    number2 = random.randint(1, 8)

    length = hypoteneuse(number1, number2)

    # The lines below uses something called an 'f-string' for string
    # formatting.  Feel free to use this as a model for making your
    # own formatted strings!
    print(f'The values I chose were {number1} and {number2}')
    print(f'The value I calculated was: {length}')

    if not (squared(length) == squared(number1) + squared(number2)):
        print('Something went wrong!  These numbers don\'t add up the way they should!')

main()
