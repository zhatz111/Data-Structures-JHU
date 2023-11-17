"""
This script takes in a frequency table, an input file for encoding, an input file for decoding,
and an output file path to encode/decode the data using a Huffman Binary Tree. It also generates
information about the Huffman tree and coding, and calculates the space reduction achieved by 
the compression.

To use this script, four arguments must be provided in the following order:
- freq_table: Required frequency table to build Huffman Binary Tree.
- text_file: Required input file for encoding a string.
- bit_file: Required input file for decoding the bits back to a string.
- output_file: Required output file path argument.

Usage:
python huffman_encoding.py freq_table.txt input.txt input_bits.txt output.txt

For encoding, the program opens the text file for reading and iterates over its lines, calculating
the Huffman encoding for each line and displaying the original string, the Huffman encoding for
that string, and the space reduction achieved by the compression.

For decoding, the program opens the bit file for reading and iterates over its lines, calculating
the Huffman decoding for each line and displaying the original bit data, the decoded string, and
the space reduction achieved by the compression.
"""

# Import Statements
# To parse the command line arguments, the argparse library is needed
# which is a standard library in python.
# The two functions imported from function are needed to remove blank lines
# in the input file and convert the expressions to postfix.
import argparse
from functions import HuffmanEncoding

# Ensure the module that this is running in is the main module
if __name__ == "__main__":
    # Create a parser instance to be able to parse command line arguments
    parser = argparse.ArgumentParser(description="This program will encode/decode \
    a test/bit file using a frequency table to build a Huffman Tree.")

    # Add an argument for the three files required by the lab assignment
    parser.add_argument("freq_table", type=str,
            help="Required frequency table to build Huffman Binary Tree")

    parser.add_argument("text_file", type=str,
            help="Required input file for encoding a string.")

    parser.add_argument("bit_file", type=str,
            help="Required input file for decoding the bits back to a string.")

    parser.add_argument("output_file", type=str,
            help="Required Output File path argument, \
            (ex: C:\\Users\\Documents\\Module 5 - Lab1\\Output.txt).")

    # To be able to access the input to the command line this is needed
    args = parser.parse_args()
    # Create an instance of the HuffmanEncoding class and build a Huffman tree
    try:
        preorder_traversal = HuffmanEncoding(args.freq_table)
        node = preorder_traversal.build_huffman_tree()

        # Generate some output about the Huffman tree
        FREQ_TABLE = ', '.join(f'{key}: {value}' for key, value in
                                preorder_traversal.freq_table.items())
        FREQ_OUTPUT = ', '.join(f'{key}: {value}' for key, value in
                                preorder_traversal.total_freq.items())
        CODE_OUTPUT = ', '.join(f'{key} = {value}' for key, value in
                                preorder_traversal.codes.items())
        # This will print out the huffman tree and coding to the console for easy inspection
        print(f"\nHuffman Tree Information (based on {args.freq_table})")
        print("------------------------")
        print(f"Frequency Table Provided: {FREQ_TABLE}\n")
        print(f"The tree in preorder is: {FREQ_OUTPUT}\n")
        print(f"The code is {CODE_OUTPUT}")
        print("------------------------\n")
        # Store all the print statements into an output text file
    
        with open(args.output_file, "a", encoding="utf-8") as f:
            print(f"\nHuffman Tree Information (based on {args.freq_table})", file=f)
            print("------------------------", file=f)
            print(f"Frequency Table Provided: {FREQ_TABLE}\n", file=f)
            print(f"The tree in preorder is: {FREQ_OUTPUT}\n", file=f)
            print(f"The code is {CODE_OUTPUT}\n", file=f)

            # Display information about the file being decoded
            print(f"\nFile to be Encoded: {args.text_file}", file=f)
            print("--------------------", file=f)

            # Create an instance of the HuffmanEncoding class for encoding
            encode = HuffmanEncoding(args.freq_table)

            # Open the binary file (string file) for reading and iterate over its lines
            with open(args.text_file, encoding="utf-8") as file:
                COUNT = 0
                temp = file.read().splitlines()
                for line in temp:
                    encoded_str = encode.huffman_encoding(line, compression_type="Encode")
                    # Display information about the current text string being encoded
                    print(f"String {COUNT}", file=f)
                    print(f"The original string: {line}", file=f)
                    print(f"Huffman Encoding for string: {encoded_str}", file=f)
                    # Calculate and display the space reduction achieved by the compression
                    encode.calculate_space_reduction(line, encoded_str, file=f)
                    # Increment the counter for the text string
                    COUNT += 1

            # Display information about the file being decoded
            print(f"\nFile to be Decoded: {args.bit_file}", file=f)
            print("--------------------", file=f)

            # Create an instance of the HuffmanEncoding class for decoding
            decode = HuffmanEncoding(args.freq_table)

            # Open the binary file (string file) for reading and iterate over its lines
            with open(args.bit_file, encoding="utf-8") as file:
                COUNT = 0
                temp = file.read().splitlines()
                for line in temp:
                    decoded_str = decode.huffman_encoding(line, compression_type="Decode")
                    # Display information about the current bit string being decoded
                    print(f"Bit String {COUNT}", file=f)
                    print(f"The original bit data: {line}", file=f)
                    print(f"Huffman Decoding from bits: {decoded_str}", file=f)
                    # Calculate and display the space reduction achieved by the compression
                    encode.calculate_space_reduction(decoded_str, line, file=f)
                    # Increment the counter for the bit string
                    COUNT += 1
            print(
                f"Huffman Encoding data was succesfully written to the output file: {args.output_file}!"
            )
    except IndexError:
        print("Huffman encoding was not succesfull. Check to ensure all text files",
              "passed to the command line contain the appropriate data.")
