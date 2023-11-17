"""This module contains functions that are needed for
assigned program to function. Namely reversing a string,
removing blank lines, and covnerting prefix to postfix.

Returns:
    str: Returns either a reversed string or a postfix string
    depending on the function being called

Yields:
    line: yields a string contained in a line of a text file
    that has the blank characters removed
"""
from stack_class import Stack

def reverse(stack, string):
    """This function will simply reverse a string that is given
    using a stack implementation.

    Args:
        stack (Stack): An instance of Stack from the Stack class
        string (str): A string that needs to be reversed

    Returns:
        str: Returns the reversed string
    """
    for count, _ in enumerate(string):
        stack.push(string[count])

    reverse_string = ""
    for _ in range(len(string)):
        reverse_string += stack.pop()
    
    return reverse_string

def remove_blanks(file):
    """This function will remove blanks from a line
    in a file using the strip function built into python.
    It then uses yeild rather than return to pause iteration
    of lines in the file and gives control back to the code
    calling this function.

    Args:
        file (file): An opened file is required to pass into this
        function so that it can iterate through each line.

    Yields:
        line: This function will yield a line in the file
        that does not contain blank values.
    """
    for L in file:
        lines = L.strip()
        if lines:
            yield lines

def prefix_to_postfix(string):
    """This function will convert a prefix expression to a postfix
    expression. It does this using a stack. A prefix string is passed
    into the function and each character is iterated through from right
    to left which is why the reverse function is called. Each character
    is checked against the operator_list for a valid operation. If a
    character is in the operator list and the stack contains greater than
    one element then the stack is popped twice and those two characters
    alogn with the operator character are combined together and pushed
    to the stack. If the character is a letter than it is automatically
    pushed to the stack. After all characters are iterated through the
    characters in the stack are joined together and the result is the
    converted postfix expression.

    Args:
        string (str): A prefix expression that needs to be converted to
        postfix

    Returns:
        str: A postfix expression
    """
    stack = Stack()
    reverse_stack = Stack()
    str_reverse = reverse(reverse_stack, string)
    operator_list = ["+","-","*","/","$","^"]

    for char in str_reverse:
        if char != " ":
            if (char in operator_list) and (len(stack.stack) > 1):
                char1 = stack.pop()
                char2 = stack.pop()
                combine = char1 + char2 + char
                stack.push(combine)
            elif char.isalpha():
                stack.push(char.upper())
            elif char not in operator_list:
                print(f"The character, {char}, passed in for line, {string},\
                      \nwas not an operand or operator and will be skipped!\n")
#
    postfix = "".join(stack.stack)
    return postfix
