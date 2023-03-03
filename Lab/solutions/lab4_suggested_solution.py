"""
INFO135 - Lab 4 suggested solutions
Note that this is simply a suggestion of how to solve the tasks, there will be many other valid
solutions. :D


Exercise 1
You have a list of length n = 8,649.
What do you think the O notation of a function is given the following amount of operations?

a) 113 115 operations = Log-Linear Complexity O(n log2 n) / O(n log n)
Big O notation ignores constants.
It's O(n log2 n) in this calculation but we ignore the base in big-O since it talks about relative growth rates.
Log2 is a constant multiplier and does not make much difference for large numbers,
so such a multiplier is irrelevant to big-O classification and reduced to O(n log n).
* in practise constant multiplies do matter, but in theory big-O looks at infinity where it is not that significant

b) 74 805 201 operations = Quadratic Complexity O(n^2)
Quadratic: steps required to execute an algorithm are a quadratic function of the number of items in the input

c) 8649 operations = Linear Complexity O(n)
Linear: steps required to execute an algorithm increase or decrease linearly with the number of items in the input


Exercise 2

def one_pass(liste, index):

    sub_liste = liste[index:]
    smallest = min(sub_liste)

    smallest_index = sub_liste.index(smallest) + index
    liste[index], liste[smallest_index] = liste[smallest_index], liste[index]

    return liste

liste = [-4,0,1,9,0]
selection_sort(liste)
# Expected output: [-4, 0, 0, 1, 9]

Above you can see the function one_pass(liste, index). This is one of the solutions to last lab’s exercise 1.
Use this function to sort an entire list.

There are two approaches to this exercise. You can choose to use one_pass(liste, index) as a helper function,
I.e. create another function that uses one_pass(liste, index) to complete a sort.
Or you can rewrite one_pass(liste, index) to recursively sort the entire list by itself.
The second approach is slightly more challenging.
"""


def one_pass(liste, index):
    """
    Sorts the given index in a list of unsorted integers and gives it the minimum value from the unsorted partition
    :param liste: unsorted list of integers
    :param index: start index that is to be sorted
    :return: returns list of integers with item with specified index sorted
    """
    sub_liste = liste[index:]
    smallest = min(sub_liste)

    smallest_index = sub_liste.index(smallest) + index
    liste[index], liste[smallest_index] = liste[smallest_index], liste[index]

    return liste


def selection_sort(li):
    """
    Uses the function one_pass to sort a whole list. Iterates over a list and pass both the list and current index to
    the one_pass function that sort the given index.
    :param li: unsorted list of integers
    :return: a fully sorted list of integers
    """
    for i in range(len(li)):
        one_pass(li, i)
    return li


def recursive_selection_sort(li, start_index):
    """
    Recursive selection sort that sorts a list of unsorted integers
    :param li: unsorted list of integers
    :param start_index: index that is to be sorted, everything to the right is unsorted
    :return: returns list of integers with item with specified index sorted
    """
    li_length = len(li)
    smallest_index = start_index
    # compare start index with integers to the right to find smallest value
    for i in range(start_index + 1, li_length):
        if li[i] < li[smallest_index]:
            smallest_index = i
    # swap values
    li[smallest_index], li[start_index] = li[start_index], li[smallest_index]
    # if there is more left to sort, calls itself to sort next integer
    if start_index + 1 < li_length:
        recursive_selection_sort(li, start_index + 1)


"""
Exercise 3: 

Given a set of n bolts of different sizes, and n bolts of different sizes there is a one to one mapping between the 
nuts and bolts. We need to find the correct matches, and assign that nut with the matching bolt. 
 
Comparison of a nut to another nut, or a bolt to another bolt is not allowed! It means that a nut can only be compared 
with a bolt, and a bolt can only be compared with a nut to see which one is bigger/smaller. 

Input: 
The lists of locks and keys: 
nuts = ['@', '#', '$', '%', '^', '&'] 
bolts = ['$', '%', '&', '^', '@', '#'] 
 
Expected output after matching nuts and bolts: 
Nuts:  #  $  %  &  @  ^ 
Bolts: #  $  %  &  @  ^ 

 
Another way of asking this problem is, given a box with locks and keys where one lock can be opened by one key in 
the box. We need to match the pair and we cannot match locks with locks or keys with keys. 
 
 
To solve this problem you will need to use quick sort (a divide and conquer algorithm), and do some slight modifications
to match the nuts and bolts. 
 
you will need to make two functions:  
def partition(array, low, high, pivot): 
def quick_sort(nuts, bolts, low, high): 
 

First perform a partition by taking the last element of the bolt as a pivot, and rearrange the list of nuts. Return the 
partition index such that nuts smaller than nuts[partition index] are on the left side, and nuts greater that 
nuts[partition index] are on the right side.  

Then using this pivot index we got we can partition the list of bolts, with nuts[pivot index} as our pivot value. After 
that is done, we apply this partitioning recursively on the left and right sub lists of both the nuts and bolts to get 
all the matches.  

 
With both of them sorted, you will then have a case where bolts[i] = nuts[i] and you have your matched lists. 

"""


def partition(li, low, high, pivot):
    """
    Similar to regular partition, but we take pivot as an argument instead
    Places the pivot element at its correct position in sorted list, and places all smaller elements than pivot to left
    of pivot and all greater elements to right of pivot
    Return the partition index of the list based on the pivot element of the other list
    :param li: list of nuts or bolt characters
    :param low: starting index
    :param high: ending index
    :param pivot: selected pivot element
    :return: final location of pivot element
    """
    i = low  # smaller element
    j = low
    while j < high:
        if li[j] < pivot:
            # When jth element is less than pivot, swap them
            li[i], li[j] = li[j], li[i]
            i += 1  # # increment index of smaller element
        elif li[j] == pivot:
            # # When jth element is equal to pivot, swap them
            li[j], li[high] = li[high], li[j]
            j -= 1
        j += 1
    li[i], li[high] = li[high], li[i]

    # Return the partition index of the list based on the pivot element of the other list
    return i


def quick_sort(nuts, bolts, low, high):
    """
    Function works just like quick sort.
    :param nuts: list of nuts characters
    :param bolts: list of bolt characters
    :param low: starting index
    :param high: ending index
    """
    if low < high:
        # partition nuts with highest bolt as pivot
        pivot = partition(nuts, low, high, bolts[high])
        # partition bolts around nuts final position, so that matching bolt also is in its final position
        partition(bolts, low, high, nuts[pivot])
        # now the nut and bolt have matching pivots, sort elements before and after partition recursively
        quick_sort(nuts, bolts, low, pivot - 1)
        quick_sort(nuts, bolts, pivot + 1, high)


if __name__ == "__main__":
    # Exercise 2
    liste = [-4, 0, 1, 9, 0]
    print(selection_sort(liste))
    # Expected output: [-4, 0, 0, 1, 9]

    # recursive_sort
    liste2 = [2, 5, 8, 0, 1, 9, -3]
    recursive_selection_sort(liste2, 0)
    print(liste2)
    # Expected output: [-3, 0, 1, 2, 5, 8, 9]

    # Exercise 3
    # Nuts and bolts are represented as characters in lists
    nuts = ['@', '#', '$', '%', '^', '&']
    bolts = ['$', '%', '&', '^', '@', '#']
    start, end = 0, len(nuts) - 1  # start and end indices of both lists (they are same length)
    quick_sort(nuts, bolts, start, end)
    print("The matched nuts and bolts: ")
    print(*nuts)
    print(*bolts)
    """
    Expected output: 
    #  $  %  &  @  ^ 
    #  $  %  &  @  ^ 
    """