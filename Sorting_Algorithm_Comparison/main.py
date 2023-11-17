"""
This script takes in command line arguments for an input directory path and an output 
file path. It then loops through each file in the input directory, reads the contents of 
the file, and performs sorting algorithms on the contents using Quicksort and Merge Sort. 
The results are written to the output file.

The command line arguments are parsed using argparse. The input directory and output file 
arguments are added to the parser. The argparse module is used to access the input to the 
command line.

The functions used in the script are imported from a separate functions file. The functions 
used are Quicksort, LinkedListMergeSort, create_linked_list, and extract_values.

The main function creates a parser instance and adds arguments to it. It then loops through 
each file in the input directory, checks if it is a file, and reads its contents. The contents 
are then passed to the Quicksort and Merge Sort functions. The Quicksort algorithm is run four 
times using different sort methods. The time taken to perform each sort is recorded. The 
results of each sort are written to the output file.
"""

import os
import time
import textwrap
import argparse
from functions import Quicksort, LinkedListMergeSort, create_linked_list, extract_values

if __name__ == "__main__":
    # Create a parser instance to be able to parse command line arguments
    parser = argparse.ArgumentParser(description="This program will encode/decode \
    a test/bit file using a frequency table to build a Huffman Tree.")

    # Add an argument for the three files required by the lab assignment
    parser.add_argument("input_directory", type=str,
            help="Directory that contains the required input files, \
            (ex: C:\\Users\\Documents\\Module 5 - Lab1).")

    parser.add_argument("output_file", type=str,
            help="Required Output File path argument, \
            (ex: C:\\Users\\Documents\\Module 5 - Lab1\\Output.txt).")

    # To be able to access the input to the command line this is needed
    args = parser.parse_args()
    # Loop through each file in the directory
    with open(args.output_file, "a", encoding="utf-8") as f:
        for filename in os.listdir(args.input_directory):
            print(f"Sorting {filename}...", end="")
            # Check if the file is a file and not a directory
            if os.path.isfile(os.path.join(args.input_directory, filename)):
                print("", file=f)
                print("", file=f)
                print(f"FILENAME: {filename}", file=f)
                print("-"*85, file=f)
                # Open the file and do something with it
                with open(os.path.join(args.input_directory, filename), 'r', encoding="utf-8") as file:
                    numbers = []
                    raw_data = []
                    for line in file:
                        line_numbers = list(map(int, line.split()))
                        numbers.extend(line_numbers)
                        raw_data.extend(line_numbers)
                linked_arr = create_linked_list(numbers)
                quicksort_1 = Quicksort(numbers)
                quicksort_2 = Quicksort(numbers)
                quicksort_3 = Quicksort(numbers)
                quicksort_4 = Quicksort(numbers)
                merge_test = LinkedListMergeSort()

                start_time_1 = time.time()
                quicksort_1.sort(sort_method="first")
                end_time_1 = time.time()

                start_time_2 = time.time()
                quicksort_2.sort(sort_method="insertion50")
                end_time_2 = time.time()

                start_time_3 = time.time()
                quicksort_3.sort(sort_method="insertion100")
                end_time_3 = time.time()

                start_time_4 = time.time()
                quicksort_4.sort(sort_method="median")
                end_time_4 = time.time()

                start_time_5 = time.time()
                merge_head = merge_test.merge_sort(linked_arr)
                end_time_5 = time.time()
                
                if len(numbers) < 101:
                    print("Original File Data:",file=f)
                    numb_arr = ' '.join(map(str, raw_data))
                    print(f"{textwrap.fill((numb_arr),85)}", file=f)
                    print("-"*85, file=f)
                    print(f"|{'Algorithm': ^20}|{'Comparisons': ^20}|{'Exchanges': ^20}|{'Time (sec)': ^20}|", file=f)
                    print("-"*85, file=f)
                    print(f"|{'First Pivot': ^20}|{quicksort_1.comparisons: ^20}|{quicksort_1.exchanges: ^20}|{end_time_1 - start_time_1: ^20.5f}|", file=f)
                    qs1_arr = ' '.join(map(str, quicksort_1.arr))
                    print(f"{textwrap.fill(qs1_arr,85)}", file=f)
                    print("-"*85, file=f)
                    print(f"|{'Insertion 50': ^20}|{quicksort_2.comparisons: ^20}|{quicksort_2.exchanges: ^20}|{end_time_2 - start_time_2: ^20.5f}|", file=f)
                    qs2_arr = ' '.join(map(str, quicksort_2.arr))
                    print(f"{textwrap.fill(qs2_arr,85)}", file=f)
                    print("-"*85, file=f)
                    print(f"|{'Insertion 100': ^20}|{quicksort_3.comparisons: ^20}|{quicksort_3.exchanges: ^20}|{end_time_3 - start_time_3: ^20.5f}|", file=f)
                    qs3_arr = ' '.join(map(str, quicksort_3.arr))
                    print(f"{textwrap.fill(qs3_arr,85)}", file=f)
                    print("-"*85, file=f)
                    print(f"|{'Median-of-Three': ^20}|{quicksort_4.comparisons: ^20}|{quicksort_4.exchanges: ^20}|{end_time_4 - start_time_4: ^20.5f}|", file=f)
                    qs4_arr = ' '.join(map(str, quicksort_4.arr))
                    print(f"{textwrap.fill(qs4_arr,85)}", file=f)
                    print("-"*85, file=f)
                    print(f"|{'Natural Merge Sort': ^20}|{merge_test.comparisons: ^20}|{merge_test.exchanges: ^20}|{end_time_5 - start_time_5: ^20.5f}|", file=f)
                    merge_arr = ' '.join(map(str, extract_values(merge_head)))
                    print(f"{textwrap.fill(merge_arr,85)}", file=f)
                    print("-"*85, file=f)
                else:
                    print("-"*85, file=f)
                    print(f"|{'Algorithm': ^20}|{'Comparisons': ^20}|{'Exchanges': ^20}|{'Time (sec)': ^20}|", file=f)
                    print("-"*85, file=f)
                    print(f"|{'First Pivot': ^20}|{quicksort_1.comparisons: ^20}|{quicksort_1.exchanges: ^20}|{end_time_1 - start_time_1: ^20.5f}|", file=f)
                    print(f"|{'Insertion 50': ^20}|{quicksort_2.comparisons: ^20}|{quicksort_2.exchanges: ^20}|{end_time_2 - start_time_2: ^20.5f}|", file=f)
                    print(f"|{'Insertion 100': ^20}|{quicksort_3.comparisons: ^20}|{quicksort_3.exchanges: ^20}|{end_time_3 - start_time_3: ^20.5f}|", file=f)
                    print(f"|{'Median-of-Three': ^20}|{quicksort_4.comparisons: ^20}|{quicksort_4.exchanges: ^20}|{end_time_4 - start_time_4: ^20.5f}|", file=f)
                    print(f"|{'Natural Merge Sort': ^20}|{merge_test.comparisons: ^20}|{merge_test.exchanges: ^20}|{end_time_5 - start_time_5: ^20.5f}|", file=f)
            print("Completed!")
        print(f"Check {args.output_file} for the result table for each file that was sorted!")
