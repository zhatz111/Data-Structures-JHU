"""This module contains functions that are needed for the
assigned program to function. Namely removing blank lines, 
and converting prefix to postfix.

Returns:
    str: Returns a postfix string

Yields:
    line: yields a string contained in a line of a text file
    that has the blank characters removed
"""

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

def prefix_to_postfix(prefix_str):
    """This function will convert a prefix expression to a postfix
    expression using recursion. It does this by first defining an
    operator list with the accepted operators that can be used in
    each prefix string. It also initializes an operator count
    variable. A helper function is used in this function that acts
    as the recursive function. This is necessary to use in order to
    perform all the error checking for prefix strings required from
    the lab. 
    The helper function works by recursively processing each 
    operator in the prefix string. If the current character is an operator, 
    it calls itself on the left and right substrings of the prefix 
    string (excluding the current operator). If both recursive calls 
    return valid postfix strings, it concatenates them with the current 
    operator and returns the result along with a True flag. If either 
    recursive call returns an invalid postfix string, it returns an empty 
    string and a False flag to indicate that the conversion was not successful.
    If the current character is an operand, the helper function simply 
    returns the current operand and a True flag.
    The main function calls the helper function on the entire prefix string 
    and checks if the conversion was successful and if the number of operators 
    in the prefix string is exactly half the length of the prefix string. If 
    either of these conditions is not met, it returns whether the prefix string
    has too many operators or whether it has too mfew operators. Otherwise, 
    it returns the final postfix string.

    Args:
        prefix_str (str): A prefix expression in string format

    Returns:
        str: This function overall will return a converted prefix string if the
        correct number of operators and operands exist in the given string. Otherwise,
        it will return an error message.
    """
    operators = ["+","-","*","/","$"]
    operator_count = 0
    
    def helper(i):
        nonlocal operator_count
        
        if i >= len(prefix_str):
            return "", True
        
        if prefix_str[i] in operators:
            operator_count += 1
            left, valid = helper(i+1)
            if not valid:
                return "", False
            right, valid = helper(i+len(left)+1)
            if not valid:
                return "", False
            return left + right + prefix_str[i], True
        elif prefix_str[i].isalpha():
            return prefix_str[i], True
        else:
            return prefix_str[i+1], True
    
    postfix_str, valid = helper(0)
    if not valid or operator_count != len(prefix_str) // 2:
        if operator_count > len(prefix_str) // 2:
            err_msg = f"Error: The prefix string '{prefix_str}' has too many Operaters!"
            print(err_msg)
            return err_msg
        if operator_count < len(prefix_str) // 2:
            err_msg = f"Error: The prefix string '{prefix_str}' has too few Operaters!"
            print(err_msg)
            return err_msg
    else:
        return postfix_str
