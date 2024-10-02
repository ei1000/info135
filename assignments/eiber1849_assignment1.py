###########################################################################################################################################################

#1

import math

#Creates a function to calc worst case binary search.
def Binary_search_worst(size):
    return math.ceil(math.log2(size))

print(f'Persian dictionary with 171476 words, would worst case take {Binary_search_worst(171476)} steps')
print(f'English dictionary with 1100373 words, would worst case take {Binary_search_worst(1100373)} steps')
print(f'Chinese dictionary with 260000 words, would worst case take {Binary_search_worst(260000)} steps')

# a) Persian dictionary with 171476 words, would worst case take 18 steps
# b) English dictionary with 1100373 words, would worst case take 21 steps
# c) Chinese dictionary with 260000 words, would worst case take 18 steps

###########################################################################################################################################################

#2

#Given linked-list class, write print_list() method. Method loops over and prints entire contents of list from head.

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    #Linked list points to the next node from the head node. When you have reached the last next node, its next node is none. 
    def print_list(self):
        x = self.head
        while x != None:
            print(x.data)
            x = x.next


#Tests to make sure it works as intended
node1 = Node('1')
node2 = Node('2')
node3 = Node('3')
node_end = Node('end_node')

t_list = LinkedList()
t_list.head = node1
node1.next = node2
node2.next = node3
node3.next = node_end

#Prints the content of the list
t_list.print_list()

###########################################################################################################################################################

#3

#Stack implementation
class Stack:
    def __init__(self) -> None:
        self.items = []
    
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    


def reverse_list(list_in=[]):
    #Building a stack with the elements of the list
    func_stack = Stack()
    for element in list_in:
        func_stack.push(element)
    
    #Reversing the stack into another stack, by transfering the top elements to the bottom of the reversed stack.
    reversed_stack = Stack()
    while func_stack.size() > 0:
        reversed_stack.push(func_stack.items.pop())

    #Then printing the reversed stack    
    print(reversed_stack.items)


#The assignment states that the function should recieve a python list, build a stack with the same elements, and then print the reversed list. 
#Here you could just build a stack, and then print the reversed input list with print(list(reversed(list_in))) or print(list[::-1]) 
#But since it states build a stack, it would be unusual to not utilize it. Hence I interpret the task to use a stack to reverse.

#Heres the other implementation just in case
# # def reverse_list(list_in=[]):
# #     #Building a stack with the elements of the list
# #     func_stack = Stack()
# #     for element in list_in:
# #         func_stack.push(element)

# #     #Then printing the reversed stack    
# #     print(list_in[::-1])

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_list(my_list)

