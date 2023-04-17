#1

#Answer b is correct.

#2

'''
If the sollution is correct, then no queens should attack eachother. If no queens are attacking, then self.examine returns self.ACCEPT, else self.ABANDON.

If the examined coandidate is equal to self.ACCEPT, then it is a solution. 

Also the candidate has to be filled, so it has to be len(candidate) = len(self.COLUMNS) 

Another way to check is if the candidate solution is a variation of the solutions. This uses the examine function in the solve function, so it would be more steps. 
'''

class Queen_n:
    def __init__(self) -> None:
        self.COLUMNS = "abcde"
        self.NUM_QUEENS = len(self.COLUMNS)
        self.ACCEPT = 1
        self.CONTINUE = 2
        self.ABANDON = 3
        self.all_solutions = []

    def solve(self, partial_sol):
        exam = self.examine(partial_sol)
        if exam == self.ACCEPT:
            print(partial_sol)
        elif exam != self.ABANDON:
            for p in self.extend(partial_sol):
                self.solve(p)

    def examine(self,partial_sol):
        for i in range(len(partial_sol)):
            for j in range(i + 1, len(partial_sol)):
                if self.attacks(partial_sol[i],
                    partial_sol[j]):
                    return self.ABANDON
        if len(partial_sol) == self.NUM_QUEENS:
            return self.ACCEPT
        else:
            return self.CONTINUE

    def attacks(self, p1, p2):
        column1 = self.COLUMNS.index(p1[0]) + 1
        row1 = int(p1[1])
        column2 = self.COLUMNS.index(p2[0]) + 1
        row2 = int(p2[1])
        return (row1 == row2 or column1 == column2 or abs(row1-row2) == abs(column1-column2))

    def extend(self, partial_sol):
        results = []
        row = len(partial_sol) + 1
        for column in self.COLUMNS:
            new_solution = list(partial_sol)
            new_solution.append(column + str(row))
            results.append(new_solution)
        return results
    
    #If no queens attack, then solution.
    def is_solution(self, candidate_solution):
        if self.examine(candidate_solution) == self.ACCEPT: # and len(candidate_solution) == len(self.COLUMNS) <- Unecessary, because examine will return 2.
            return 'Valid!'
        else:
            return 'Invalid!'
    
    
candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']
board = Queen_n()
board.extend('f')
result1 = board.is_solution(candidate_solution1)
result2 = board.is_solution(candidate_solution2)
print("Candidate Solution 1:", result1)
print("Candidate Solution 2:", result2)



######################################################################################################################################################################

#Implementation of Graph class:

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
            if node in self.graph:
                for neighbour in self.graph[node]:
                    self.depth_first_search(neighbour)
    
    def find_cycle_cheesy(self, node):
        try:
            self.depth_first_search(node)
            return 'Cycle has not been found'
        except RecursionError:
            return 'Cycle has been found'
        
    def find_cycle(self, node):
        state = {node: 'Not_visited' for node in self.graph.keys()}
        
        def dfs(node, state):
            state[node] = 'Visited'
            for neighbour in self.graph[node]:
                if neighbour in state and state[neighbour] == 'Visited':
                    return 1
                elif neighbour in state and state[neighbour] == 'Not_visited':
                    return dfs(neighbour, state)

        if node not in self.graph.keys():
            return "Starting on bottom node, no cycle!"

        elif dfs(node, state) == 1:
            return 'Cycle found!'
        else:
            return 'No cycle found'

    def print_graph(self):
        print(self.graph)

#3

'''
To find a cycle, you have to start a search from one node, and end up at the same node again. If you use DFS, then you will sort of loop in the cycle, when its found.

A simple way to look out for a cycle is to "mark" the nodes during the search. Have this node been visited before, then it is marked as visited, and you continue the search.

If you encounter the "depth" or "bottom", you mark this as "bottom", meaning no more edges. And no possibility for a cycle with that node.

The function is to do a search from the node, mark it as visited, check it's neighbours and do the same. When it encounters a node that is "bottom", then there are no cycles on that route.

It then checks the other neighbours, and their neighbours. 

If it encounters an already visited node, than a cycle has been found. 
'''

def find_cycle(self, node):
        state = {node: 'Not_visited' for node in self.graph.keys()}
        
        def dfs(node, state):
            state[node] = 'Visited'
            for neighbour in self.graph[node]:
                if neighbour in state and state[neighbour] == 'Visited':
                    return 1
                elif neighbour in state and state[neighbour] == 'Not_visited':
                    return dfs(neighbour, state)

        if node not in self.graph.keys():
            return "Starting on bottom node, no cycle!"

        elif dfs(node, state) == 1:
            return 'Cycle found!'
        else:
            return 'No cycle found'

my_graph = Graph()
my_graph.add_edge('A', 'B')
my_graph.add_edge('B', 'D')
my_graph.add_edge('C', 'B')
my_graph.add_edge('C', 'J')
my_graph.add_edge('D', 'E')
my_graph.add_edge('D', 'F')
my_graph.add_edge('E', 'C')
my_graph.add_edge('E', 'G')
my_graph.add_edge('F', 'H')
my_graph.add_edge('G', 'I')
my_graph.print_graph()
result = my_graph.find_cycle('J')
print(result)

#4

'''
Ive implemented this above in excersice 3. It looks like this. It deletes all the edges from a node and to the node. 
'''

def remove_node(self, node):
        for nodes in self.graph.keys():
            if nodes in self.graph.keys():
                if node in self.graph[nodes]:
                    self.graph[nodes].remove(node)
        self.graph.pop(node, None)

graph = Graph()
graph.add_edge('a', 'b')
graph.add_edge('a', 'c')
graph.add_edge('b', 'c')
graph.add_edge('b', 'd')
graph.add_edge('b', 'a')
graph.add_edge('c', 'd')
graph.add_edge('d', 'e')
graph.add_edge('e', 'd')
graph.print_graph()
#result = graph.find_cycle('b')
#print(result)
graph.remove_node('a')
print('after removal:')
graph.print_graph()