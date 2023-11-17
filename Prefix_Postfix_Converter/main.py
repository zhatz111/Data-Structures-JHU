"""This is the main module that will parse the command line arguments for the 
input and output text and run the prefix_to_postfix function to convert each
expression in the text file. This will also remove any blank lines that
may occur accidentally in the input file.
"""

# Import Statements
# To parse the command line arguments, the argparse library is needed
# which is a standard library in python
# The two functions imported from function are needed to remove blank lines
# in the input file and convert the expressions to postfix
import argparse
from functions import remove_blanks, prefix_to_postfix

# Ensure the module that this is running in is the main module
if __name__ == "__main__":
    # Create a parser instance to be able to parse command line arguments
    parser = argparse.ArgumentParser(description='This program will convert a \
            Prefix expression to a Postfix expression that is given in a text file')
    # Add an argument for the input and output file
    parser.add_argument('input_file', type=str,
            help='Required Input File path argument, \
            (ex: C:\\Users\\Documents\\Module 5 - Lab1\\Required_Input.txt).')
    parser.add_argument('output_file', type=str,
            help='Required Output File path argument, \
            (ex: C:\\Users\\Documents\\Module 5 - Lab1\\Output.txt).')
    # To be able to access the input to the command line this is needed
    args = parser.parse_args()
    # Open the input and output files from the command line arguments
    output = open(args.output_file, "a", encoding="utf-8")
    with open(args.input_file, encoding="utf-8") as file:
        # Iterate through each line in the input file
        # passing it through the remove blanks file which yeilds 
        # the line without blank characters
        for line in remove_blanks(file):
            # First convert the lines prefix expression to postfix
            # then write that converted line to the output file
            # and write a new line as well to match format of
            # input file
            output.write(prefix_to_postfix(line))
            output.write('\n')
