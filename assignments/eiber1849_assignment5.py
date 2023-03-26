#1

#All of the trees are full binary trees, because all of the interior nodes has 2 children, and the rest has none. 

#2

def binary_tree(root):
    return [root, [], []]

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

def get_root(root):
    return root[0]

def insert_left_child(root, newbranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newbranch, t, []])
    else:
        root.insert(1, [newbranch, [], []])
    return root

def insert_right_child(root, newbranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newbranch, [], t])
    else:
        root.insert(2, [newbranch, [], []])
    return root

def make_tree():
    root = binary_tree(1)
    insert_left_child(root, 2)
    insert_right_child(root, 3)
    insert_left_child(get_left_child(root), 4)
    insert_left_child(get_right_child(root), 5)
    insert_right_child(get_right_child(root), 6)
    return root


#print(make_tree())

#3

class Graph:
    def __init__(self) -> None:
        self.graph = dict()
        self.d_search = []
    
    def add_edge(self, node, neighbour):
        if node not in self.graph:
            self.graph[node] = [neighbour]
        else:
            self.graph[node].append(neighbour)
    
    def check_neighboor(self, node1, node2):
        return node2 in self.breadth_first_search(node1)
    
    def find_all_nodes(self):
        all_nodes = []
        for node, edges in self.graph.items():
            if node not in all_nodes:
                all_nodes += node
            for node in edges:
                if node not in all_nodes:
                    all_nodes += node
        return all_nodes
    
    def remove_edge(self, node1, node2):
        try:
            if self.check_neighboor(node1, node2):
                if len(self.graph[node1]) == 1:
                    self.graph.pop(node1, None)
                else:
                    self.graph[node1].remove(node2)
                print(f'removed {node2} from {node1}')
        except KeyError:
            print('The nodes are not neighboors')
    
    def remove_node(self, node):
        for nodes in self.graph.keys():
            if nodes in self.graph.keys():
                if node in self.graph[nodes]:
                    self.graph[nodes].remove(node)
        self.graph.pop(node, None)


    def nodes_out_degree(self, n):
        points = [key for key, valu in self.graph.items() if len(valu) == n]
        print(points)
        return points
    
    def breadth_first_search(self, node):
        
        searched = [node]
        search_queue = [node]

        while search_queue:
            node = search_queue.pop(0)

            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour not in searched:
                        searched.append(neighbour)
                        search_queue.append(neighbour)
        return searched
    

    def depth_first_search(self, node):
        searched = []
        if node not in searched:
            searched.append(node)
            print(node)
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)

    

def build_my_graph():
    graph = Graph()
    graph.add_edge('a', 'b')
    graph.add_edge('a', 'c')
    graph.add_edge('b', 'c')
    graph.add_edge('b', 'd')
    graph.add_edge('c', 'e')
    graph.add_edge('d', 'e')
    graph.add_edge('d', 'g')
    graph.add_edge('d', 'h')
    graph.add_edge('e', 'f')
    graph.add_edge('f', 'c')
    return graph.depth_first_search('a')

#print(build_my_graph())

#It starts the search, but when it enters c it gets stuck in a cycle. So you get c-e-f-c-e-f-c-e-f etc. And eventually an RecursionError is raised.

#4

class BinarySearchTree:
    def __init__(self, value=None) -> None:
        self.value = value
        if self.value:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None
    
    def is_empty(self):
        if self.value == None:
            return 1
        else:
            return None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        elif value < self.value:
            self.left_child.insert(value)
        elif value > self.value:
            self.right_child.insert(value)
    
    def in_order(self):
        if self.is_empty():
            return []
        else:
            return self.left_child.in_order() + [self.value] + self.right_child.in_order()
    
    #If i use the in_order method, and pythons in build functions

    def compute_sum(self):
        in_order = self.in_order()
        return sum(in_order)

    def compute_count(self):
        in_order = self.in_order()
        return len(in_order)
    
    #My own implementation. This is quite similar to the fibonacci calculation. 
    def compute_sum(self, tree = None):
        left = tree.left_child
        right = tree.right_child
        if left == None and right == None:
            return 0
        else:
            return self.compute_sum(left) + tree.value + self.compute_sum(right)
    
    def compute_count(self, tree=None):
        left = tree.left_child
        right = tree.right_child
        if left == None and right == None:
            return []
        else:
            return self.compute_sum(left) + [tree.value] + self.compute_sum(right)


    def print_tree(self):
        print(self.in_order())


my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(8)
my_tree.insert(10)
print('sum:', my_tree.compute_sum(my_tree))
print('number of nodes:', my_tree.compute_count(my_tree))
