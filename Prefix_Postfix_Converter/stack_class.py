"""This module contains the Stack ADT implementation
needed for use in converting a prefix expression to a
postfix expression.

Returns:
    Stack: Returns a Stack instance
"""
class Stack():
    """This class is my implementation of a stack ADT using
    the built in python list data structure. The methods in
    this class are isempty, pop and push which are typical
    methods described in lecture regarding the stack ADT.
    """

    def __init__(self):
        self.stack = []

    def isempty(self):
        """This method will check whether the stack
        is empty.

        Returns:
            bool: Returns either True or False
        """
        if len(self.stack) == 0:
            return True
        else:
            return False

    def pop(self):
        """This method will remove the top element of
        the stack and return its value. If the isempty
        returns True then the pop will not proceed and
        will instead print that the stack is underflowing
        In the case of this assignment the value will be 
        a character.

        Returns:
            char: Returns whatever the value of the
            top element of the stack is
        """
        if self.isempty():
            return print("Stack Underflow!")
        else:
            return self.stack.pop()

    def push(self, char):
        """This method will push a character to the stack
        using python's list append function. 

        Args:
            char (char): Specify a character to push to the
            stack

        Returns:
            stack: Returns a stack object with the specified
            character pushed to the stack
        """
        return self.stack.append(char)
