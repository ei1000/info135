"""
INFO135 - Lab 3 suggested solutions
Note that this is simply a suggestion of how to solve the tasks, there will be many other valid
solutions. :D


OBS! In this file you will se type hints in the code. Type hints help document your code, and improve IDEs and linters.

Here is a quick explanation of what it means if it is confusing:

Here is a normal function with type hints:
def func(arg: arg_type) -> return_type:

For arguments the syntax is argument: annotation, while the return type is annotated using -> annotation.

Here we say that both the arguments are of the type int, and the return type is also of the type int.
def plus(num1: int, num2: int) -> int:
    return num1 + num2

if there is -> None behind a function, it means that the function does not have a return statement

If you're interested in reading more about this, here are two guides on type hints in python:
https://realpython.com/python-type-checking/
https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html

* type hinting is not something one must do, it a optional feature ;)
"""
from typing import List, Tuple
from typing import Tuple

"""
Exercise 1

Write a function that performs exactly one pass of selection sort on any given list of integers.

Example:
selection_sort_one_pass([5, 2, 3, 4, 0, 1])
>> > [0, 2, 3, 4, 5, 1]

 """

unsorted_list: List[int] = [5, 2, 3, 4, 0, 1]


def one_pass(li: List[int], index: int) -> List[int]:
    """
    The first item in a unsorted partition is compared with all the values to the right-hand side to check if it is
    the minimum value. If it is not the minimum value, then its position is swapped with the minimum value.
    :param li: an unsorted list containing integers
    :param index: Indicate the left most item (first position) in the unsorted partition by index
    :return: list containing integers, with one sorted pass performed
    """
    # Create sublist from first position, where the leftmost value (index) is the start of the partition
    sub_list = li[index:]
    # Find the minimum element in the unsorted subarray
    smallest = min(sub_list)
    # Find the index of the minimum element on the right hand side of first position
    # sub_list.index(smallest) excludes values not in sub_list, does not start at index 0 of li
    # to find real index in li (argument), we make up for potential items on the left side of sub_list hence + index
    smallest_index = sub_list.index(smallest) + index

    # Swap the found minimum element with the first element
    # The first position takes the position previously held by the lower value, and
    # The lower value from the right-hand side takes the first position
    li[index], li[smallest_index] = li[smallest_index], li[index]

    """
    # Python allows us to switch the elements with a = b, b = a in one line as seen on the line above ^
    # Another way to switch the values is to hold them in temp variable like so:
    # The leftmost value (index) is stored in a temporal variable
    temp = li[index]
    # The lower value from the right-hand side takes the first position in the list
    li[index] = li[smallest_index]
    # The value stored in the temporal value is stored in the position that was previously held by the minimum value
    li[smallest_index] = temp
    """

    # Returns the list as the function result
    return li


# print the unsorted list
print(f"Unsorted list: {unsorted_list}")
# Print the list after calling the one pass function, passing in unsorted list as the parameter
print(f"One pass result: {one_pass(unsorted_list, 0)}")
print()  # Create empty line before next print to separate exercises prints

"""
Exercise 2 

File large_list.py contains a list of 104.6 tuples each containing 3 numbers. Write an algorithm that iterates 
through each tuple and creates a new list containing each tuple where the sum of index 0 and 1 equal index 2. 

Sort the new list containing only valid tuples so that the last elements of the tuples are in ascending order.  
Use a sorting algorithm of your choice. 

Example: 

>>> tuples = [(0,0,1), (0,1,1), (0,1,2), (1,1,2), (1,2,3)] 
>>> tuples = filter_tuples(tuples) 
>>> selection_sort(tuples) 
> [(0,1,1), (1,1,2), (1,2,3)] 
"""
# Import variable 'liste' from the file large_list.py
from large_list import liste


def filter_tuples(t_list: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Function that iterates through each tuple in a list and creates a new list containing each tuple where the sum of
    index 0 and 1 equal index 2
    :param t_list: a list consisting of tuples with 3 int values
    :return: a list consisting of tuples with 3 int values
    """
    # Create empty list
    tuple_list = []
    # Traverse through all tuples in list
    for tup in t_list:
        # if tuple 1 + 2 = 3, then append that tuple to the new tuple_list
        if tup[0] + tup[1] == tup[2]:
            tuple_list.append(tuple(tup))
    return tuple_list


# Same thing, but list comprehension (more compact and faster solution with shorter syntax)
def alternative_filter(t_list: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Function that iterates through each tuple in a list and creates a new list containing each tuple where the sum of
    index 0 and 1 equal index 2
    :param t_list: a list consisting of tuples with 3 int values
    :return: a list consisting of tuples with 3 int values
    """
    tuple_list = [tup for tup in t_list if tup[0] + tup[1] == tup[2]]
    return tuple_list


def selection_sort(t_list: List[Tuple[int, int, int]]) -> None:
    """
    A selection sort algorithm, sorts a list of tuples so that the last elements of the tuples are in ascending order
    :param t_list: a list consisting of tuples with 3 int values
    """
    # sort by third element of tuple, set nth to be 2
    nth = 2
    # Traverse through all tuples in list
    for index in range(len(t_list)):

        # Set index to be the minimum element in the unsorted list
        smallest_index = index
        #  Compare the leftmost value to the other values on the right-hand side
        # J does not start at 0, but at 'index + 1', this excludes values that have been sorted
        for j in range(index + 1, len(t_list)):
            # Finds the minimum value in the unsorted list and places it in its proper position
            # [nth] sort by the nth element of tuple
            if t_list[smallest_index][nth] > t_list[j][nth]:
                # Update smallest value if the condition is true
                smallest_index = j

        # Swap the found minimum element with the first element
        t_list[index], t_list[smallest_index] = t_list[smallest_index], t_list[index]


# Call the filter function, passing in the variable 'liste' from the file large_list.py
tuples = filter_tuples(liste)
# Sort the list tuples
selection_sort(tuples)
# Print the now sorted list tuples
print(tuples)

"""
Exercise 3

Write a function that can take in two strings as function arguments and determine if they are anagrams or not, 
and print the result in the console. An anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase. Two words are anagrams of each other if they contain the same number of characters and the same 
amount of each character. 

Examples of anagrams are as follows: abc = cba, ABBA = baba, Cat = Act, 
Astronomer = Moon starer, The Detectives = Detect Thieves, Funeral = Real fun, Listen = Silent. 

You need to sort the characters in lexicographic order (alphabetical order), and determine if all the characters in 
one string are equal to and in the same order as all the characters in the other string. To allow for strings with 
upper case letters and phrases with spaces, you should convert the string values into lowercase and remove spaces 
before you sort the characters. 

You are not allowed to do this the easy way and use inbuilt functions such as the sorted() function, you must utilize 
another sorting algorithm of your choice (Like bubble sort, selection sort, insertion sort etc). 
"""


def bubble_sort(str_list: List[str]) -> None:
    """
    A bubble sort algorithm, that sorts a list of string values in lexicographic order (alphabetical order).
    :param str_list: List: a list of string values that is to be sorted
    """
    # Assign length of the list to variable
    list_length = len(str_list)

    # Traverse through all list elements starting from 0, stopping before last element. We could use only list_length,
    # but outer loop will repeat one time more than needed since second to last item will compare to last item, hence -1
    for i in range(list_length - 1):

        # Inner loop that compares all the values in the list from the first to the last one
        for j in range(0, list_length - 1):
            """ If you want to see step by step of the bubble sort in console, uncomment the print statement below! """
            # print(str_list)
            # Check if the value on the left-hand side is greater than the one on the immediate right side
            if str_list[j] > str_list[j + 1]:
                # Swap elements if the element found is greater than the next element
                str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]


def anagram_checker(s1: str, s2: str) -> None:
    """
    A function that checks if two string values are anagrams of each other
    :param s1: a string value
    :param s2: a string value
    """
    string1, string2 = clean_strings(s1, s2)

    # Comparing the length of the strings, if not the same length, they are not anagrams
    if len(string1) != len(string2):
        print("The strings are not the same length, therefore they are not anagrams")
    else:
        # Sorting the strings with our sorting algorithm
        bubble_sort(string1)
        bubble_sort(string2)
        # Recap: If a input was 'silent' it became a list with the characters: ['l', 'i', 's', 't', 'e', 'n']
        # Recap: After the sorting algorithm, it is now sorted alphabetically like so: ['e', 'i', 'l', 'n', 's', 't']
        # Check if the two strings are equal/identical and match character by character
        # if both the lists are identical, and the elements at the same position, they are in fact anagrams
        if string1 == string2:
            # use f-print to print the original string values, and confirm that they are anagrams
            print(f"The strings '{s1}' and '{s2}' are anagrams")
        else:
            print(f"The strings '{s1}' and '{s2}' NOT anagrams")


def clean_strings(s1: str, s2: str) -> Tuple[List[str], List[str]]:
    """
       Processes two string values. Removes spaces, converts values to all lowercase and convert them to lists
       :param s1: a string value
       :param s2: a string value
       :return: returns a tuple containing the processed string1 and string2 values in list form
       """
    # Replace whitespace with no space, and convert the strings to all lower case letters
    # Fun fact! Python strings are immutable, and when manipulating them with functions, such as replace(), and lower(),
    # they return a new string that we must explicitly assign to a variable in order to change the string value.
    string1 = s1.replace(" ", "").lower()
    string2 = s2.replace(" ", "").lower()
    # Create list, return the string values as lists. 'cat' becomes ['c', 'a', 't']
    string1, string2 = list(string1), list(string2)
    return string1, string2


# a list of string that may or may not be anagrams
potential_anagrams: List[Tuple[str, str]] = [('abc', 'cda'), ('ABBA', 'baba'), ('Cat', 'adt'),
                                             ('The Detectives','Detect Thieves'),('Listten', 'Silent')]

print()  # make empty line to separate from last print
# for each tuple in the list potential_anagrams, check if the pair is an anagram
for string in potential_anagrams:
    anagram_checker(string[0], string[1])
