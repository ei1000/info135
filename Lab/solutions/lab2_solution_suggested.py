# Solution Suggestion for Lab 2 Exercises
# Linked Lists

# a)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# b - create nodes with values
node1 = Node('First node')
node2 = Node('Second node')
node3 = Node('Third node')

# link nodes together
node1.next = node2
node2.next = node3

# you can test that the values is stores by printing the data instance variable of a node
print(node1.data)

# we can test that they are linked correctly by printing a node (data field) with next
print(node1.next.data)


# c)
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, new_data):
        """
        add node at end of linked list.
        :param new_data: value of item we want to insert
        """
        new_node = Node(new_data)
        # Check if list is empty. if empty, insert node as head
        if self.head is None:
            self.head = new_node
            return

        node = self.head  # counter - find start node
        # iterate through list to find last item
        # terminates when last node is found
        while node.next:
            node = node.next
        # set reference of the last node to point to our new node
        node.next = new_node

    # add node to the beginning of linked list
    def add_at_beginning(self, new_data):
        new_node = Node(new_data)  # create node
        new_node.next = self.head  # set reference of node to point to head
        self.head = new_node  # change head to be the new node


# create linkedlist and add nodes to linked list
my_list = LinkedList()
my_list.add(1)
my_list.add(2)
my_list.add(3)
my_list.add_at_beginning(0)

# print elements from list by printing head, and references to other nodes
'''
This is a very bad way to print the entire list. This is hardcoded static code.
To print an entire list its better to use a while loop so it adapts to the list length! 
if i add or delete a node, it will not print. a loop that finds every node and prints it is better.  
'''
print(my_list.head.data)
print(my_list.head.next.data)
print(my_list.head.next.next.data)
print(my_list.head.next.next.next.data)
