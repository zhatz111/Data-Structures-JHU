"""
The file defines a Quicksort class that provides methods to perform quicksort on a list of integers. 
The class has four different methods to perform quicksort based on different pivot selection techniques, 
and a method to perform insertion sort for small sublists.

The Quicksort class contains three attributes:

arr: a list of integers to be sorted
comparisons: the number of comparisons made during sorting
exchanges: the number of exchanges made during sorting
The class has the following methods:

sort(): Sorts the list using a specified method. The method of sorting is specified by sort_method parameter 
which can be one of the four pivot selection techniques or the insertion sort.
    quicksort_first_pivot(): Sorts the list using the first element as the pivot.
    quicksort_insertion_100(): Sorts the list using insertion sort for sublists with length <= 100.
    quicksort_insertion_50(): Sorts the list using insertion sort for sublists with length <= 50.
    quicksort_median_of_three(): Sorts the list using the median of three elements as the pivot.
    insertion_sort(): Performs insertion sort on a list.

Each method takes a list of integers as an argument and returns the sorted list of integers. The sort() 
method is the main method that uses one of the four pivot selection techniques to sort the given list. 
If no parameter is passed to the sort() method, it uses the first element as the pivot by default. The 
class also initializes the comparisons and exchanges attributes to zero and sets the recursion limit for 
the Python interpreter.

This file also defines a class ListNode that represents a node in a linked list, and a class LinkedListMergeSort 
that represents a linked list and provides a method for sorting the list using the natural merge sort algorithm.

The ListNode class has two attributes: val, which represents the value of the node, and next, which is a 
pointer to the next node in the linked list. The class also has an __init__ method that initializes a new 
instance of the class.

The LinkedListMergeSort class has three attributes: head, which is a pointer to the head of the linked list, 
comparisons, which is an integer representing the number of value comparisons made during sorting, and exchanges, 
which is an integer representing the number of value exchanges made during sorting. The class also has three 
methods: __init__, which initializes a new instance of the class, merge_sort, which recursively sorts the linked 
list using the merge sort algorithm, and split_list and merge_lists, which are helper methods for merge_sort.

The code also includes two helper functions: create_linked_list, which creates a linked list from a list of 
values, and extract_values, which extracts the values from a linked list.
"""


class Quicksort:
    """
    A class for performing quicksort on a list of integers.

    Attributes:
    - arr (list[int]): the list of integers to be sorted
    - comparisons (int): the number of comparisons made during sorting
    - exchanges (int): the number of exchanges made during sorting

    Methods:
    - sort(sort_method="first"): Sorts the list using a specified method:
        - sort_method (str): The method of sorting to use. Defaults to "first".
            - "first": Uses the first element as the pivot
            - "insertion100": Uses insertion sort for sublists <= 100
            - "insertion50": Uses insertion sort for sublists <= 50
            - "median": Uses the median of three elements as the pivot
    - quicksort_first_pivot(arr): Sorts the list using the first element as the pivot.
    - quicksort_insertion_100(arr): Sorts the list using insertion sort for sublists <= 100.
    - quicksort_insertion_50(arr): Sorts the list using insertion sort for sublists <= 50.
    - quicksort_median_of_three(arr): Sorts the list using the median of three elements as the pivot.
    - insertion_sort(arr): Performs insertion sort on a list.
    """

    def __init__(self, arr):
        """
        Initializes a new instance of the Quicksort class.

        Args:
        - arr (list[int]): The list of integers to be sorted.
        """
        self.arr = arr
        self.comparisons = 0
        self.exchanges = 0
        from sys import setrecursionlimit
        setrecursionlimit(30000)

    def sort(self, sort_method = "first"):
        """
        Sorts the list using a specified method.

        Args:
        - sort_method (str): The method of sorting to use. Defaults to "first".
            - "first": Uses the first element as the pivot
            - "insertion100": Uses insertion sort for sublists <= 100
            - "insertion50": Uses insertion sort for sublists <= 50
            - "median": Uses the median of three elements as the pivot
        """
        if sort_method == "first":
            self.quicksort_first_pivot(self.arr)
        elif sort_method == "insertion100":
            self.quicksort_insertion_100(self.arr)
        elif sort_method == "insertion50":
            self.quicksort_insertion_50(self.arr)
        elif sort_method == "median":
            self.quicksort_median_of_three(self.arr)

    def quicksort_first_pivot(self, arr):
        """
        Sorts the list using the first element as the pivot.

        Args:
        - arr (list[int]): The list of integers to be sorted.

        Returns:
        - sorted_list (list[int]): The sorted list of integers.
        """
        if len(arr) <= 1:
            return arr

        if len(arr) == 2:
            self.comparisons += 1
            if arr[0] <= arr[1]:
                return arr
            else:
                self.exchanges += 1
                return [arr[1], arr[0]]

        pivot = arr[0]
        smaller, equal, larger = [], [], []
        for element in arr:
            self.comparisons += 1
            if element < pivot:
                smaller.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                larger.append(element)
        return self.quicksort_first_pivot(smaller) + equal + self.quicksort_first_pivot(larger)

    def quicksort_insertion_100(self, arr):
        """
        Sorts the given list `arr` using the quicksort algorithm with insertion sort optimization 
        for subarrays of length <= 100.

        Args:
            arr (list): The list to be sorted.

        Returns:
            list: The sorted list.

        """
        if len(arr) <= 1:
            return arr

        if len(arr) == 2:
            self.comparisons += 1
            if arr[0] <= arr[1]:
                return arr
            else:
                self.exchanges += 1
                return [arr[1], arr[0]]

        if len(arr) <= 100:
            return self.insertion_sort(arr)

        pivot = arr[0]
        smaller, equal, larger = [], [], []
        for element in arr:
            self.comparisons += 1
            if element < pivot:
                smaller.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                larger.append(element)
        return self.quicksort_insertion_100(smaller) + equal + self.quicksort_insertion_100(larger)

    def quicksort_insertion_50(self, arr):
        """
        Sorts the given array in non-descending order using quicksort algorithm
        with insertion sort for subarrays with length <= 50.

        Args:
            arr (list): The input list to be sorted.

        Returns:
            list: The sorted list in non-descending order.
        """
        if len(arr) <= 1:
            return arr

        if len(arr) == 2:
            self.comparisons += 1
            if arr[0] <= arr[1]:
                return arr
            else:
                self.exchanges += 1
                return [arr[1], arr[0]]

        if len(arr) <= 50:
            return self.insertion_sort(arr)

        pivot = arr[0]
        smaller, equal, larger = [], [], []
        for element in arr:
            self.comparisons += 1
            if element < pivot:
                smaller.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                larger.append(element)
        return self.quicksort_insertion_50(smaller) + equal + self.quicksort_insertion_50(larger)

    def quicksort_median_of_three(self, arr):
        """
        Sorts the given array in non-descending order using quicksort algorithm
        with median-of-three pivot selection.

        Args:
            arr (list): The input list to be sorted.

        Returns:
            list: The sorted list in non-descending order.
        """
        if len(arr) <= 1:
            return arr

        if len(arr) == 2:
            self.comparisons += 1
            if arr[0] <= arr[1]:
                return arr
            else:
                self.exchanges += 1
                return [arr[1], arr[0]]

        # select pivot as median of first, last, and middle elements
        first = arr[0]
        last = arr[-1]
        middle = arr[len(arr)//2]
        if first <= middle <= last or last <= middle <= first:
            pivot = middle
        elif middle <= first <= last or last <= first <= middle:
            pivot = first
        else:
            pivot = last

        smaller, equal, larger = [], [], []
        for element in arr:
            self.comparisons += 1
            if element < pivot:
                smaller.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                larger.append(element)
        return self.quicksort_median_of_three(smaller) + equal + self.quicksort_median_of_three(larger)

    def insertion_sort(self, arr):
        """
        Sorts the given array in non-descending order using insertion sort algorithm.

        Args:
            arr (list): The input list to be sorted.

        Returns:
            list: The sorted list in non-descending order.
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                self.comparisons += 1
                self.exchanges += 1
                arr[j+1] = arr[j]
                j -= 1
            self.exchanges += 1
            arr[j+1] = key
        return arr

class ListNode:
    """
    A class that represents a node in a linked list.

    Attributes:
    - val: An integer representing the value of the node.
    - next: A pointer to the next node in the linked list.

    Methods:
    - __init__(self, val=0, next=None): Initializes a new instance of the ListNode class.
    """

    def __init__(self, val=0, next=None):
        """
        Initializes a new instance of the ListNode class.

        Args:
        - val: An integer representing the value of the node. Default is 0.
        - next: A pointer to the next node in the linked list. Default is None.
        """
        self.val = val
        self.next = next


class LinkedListMergeSort:
    """
    A class that represents a linked list and provides a method for sorting the list using 
    the merge sort algorithm.

    Attributes:
    - head: A pointer to the head of the linked list.
    - comparisons: An integer representing the number of value comparisons made during sorting.
    - exchanges: An integer representing the number of value exchanges made during sorting.

    Methods:
    - __init__(self): Initializes a new instance of the LinkedListMergeSort class.
    - merge_sort(self, head): Recursively sorts the linked list using the merge sort algorithm.
    - split_list(self, head): Splits the linked list into two halves.
    - merge_lists(self, left_head, right_head): Merges two sorted linked lists into a single 
      sorted list.
    """

    def __init__(self):
        """
        Initializes a new instance of the LinkedListMergeSort class.
        """
        self.head = None
        self.comparisons = 0
        self.exchanges = 0

    def merge_sort(self, head):
        """
        Recursively sorts the linked list using the merge sort algorithm.

        Args:
        - head: A pointer to the head of the linked list to be sorted.

        Returns:
        - A pointer to the head of the sorted linked list.
        """
        if head is None or head.next is None:
            return head

        # split the list into two halves
        left_head, right_head = self.split_list(head)

        # recursively sort the left and right halves
        left_head = self.merge_sort(left_head)
        right_head = self.merge_sort(right_head)

        # merge the sorted halves
        return self.merge_lists(left_head, right_head)

    def split_list(self, head):
        """
        Splits the linked list into two halves.

        Args:
        - head: A pointer to the head of the linked list to be split.

        Returns:
        - Two pointers to the heads of the two halves of the split linked list.
        """
        # find the middle node
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # split the list in half
        left_head = head
        right_head = slow.next
        slow.next = None

        return left_head, right_head

    def merge_lists(self, left_head, right_head):
        """
        Merges two sorted linked lists into a single sorted list.

        Args:
        - left_head: A pointer to the head of the left sorted linked list to be merged.
        - right_head: A pointer to the head of the right sorted linked list to be merged.

        Returns:
        - A pointer to the head of the merged sorted linked list.
        """
        dummy = ListNode(0)
        tail = dummy

        while left_head and right_head:
            self.comparisons += 1
            if left_head.val < right_head.val:
                tail.next = left_head
                left_head = left_head.next
            else:
                tail.next = right_head
                right_head = right_head.next
                self.exchanges += 1
            tail = tail.next

        tail.next = left_head or right_head

        return dummy.next


def create_linked_list(values):
    """
    Creates a linked list from a list of values.

    Args:
        values: A list of values to be used as the node values.

    Returns:
        The head node of the linked list.
    """
    head = None
    curr = None

    for val in values:
        node = ListNode(val)
        if not head:
            head = node
            curr = node
        else:
            curr.next = node
            curr = node

    return head

def extract_values(head):
    """
    Extracts the values from a linked list.

    Args:
        head: The head node of the linked list.

    Returns:
        A list of values from the linked list.
    """
    values = []
    curr = head

    while curr:
        values.append(curr.val)
        curr = curr.next

    return values
