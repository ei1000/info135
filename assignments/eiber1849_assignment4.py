#1

#Answer b is correct.

#2
class Queen_n:
    COLUMNS = "abcde"
    NUM_QUEENS = len(COLUMNS)
    ACCEPT = 1
    CONTINUE = 2
    ABANDON = 3
    all_solutions = []
    def solve(partial_sol):...
    def examine(partial_sol):...
    def attacks(p1, p2):...
    def extend(partial_sol):...
    def is_solution(candidate_solution):
        #[your code here]
        pass
    candidate_solution1 = ['d3', 'c1', 'e5', 'b4', 'a2']
    candidate_solution2 = ['e4', 'a1', 'c5', 'd2', 'b1']
    result1 = is_solution(candidate_solution1)
    result2 = is_solution(candidate_solution2)
    print("Candidate Solution 1:", result1)
    print("Candidate Solution 2:", result2)


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
        for nodes in self.breadth_first_search(node):
            if nodes in self.graph.keys():
                if node in self.graph[nodes]:
                    self.graph[nodes].remove(node)
        self.graph.pop(node, None)


    def nodes_out_degree(self, n):
        # points = []
        # for key, valu in self.graph.items():
        #     if len(valu) == n:
        #         points += key
        # print(points)

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
            print('Cycle has not been found')
        except RecursionError:
            print('Cycle has been found')
        
    def find_cycle(self, node):
                
        searched = [node]
        search_queue = [node]

        while search_queue:
            node = search_queue.pop(0)

            if node in self.graph:
                for neighbour in self.graph[node]:
                    if neighbour in searched:
                        return 'Cycle found!'
                    elif neighbour not in searched:
                        searched.append(neighbour)
                        search_queue.append(neighbour)
                        
        return 'Cycle not found :('

            

    def print_graph(self):
        print(self.graph)

graph = Graph()
graph.add_edge('a', 'b')
graph.add_edge('a', 'c')
graph.add_edge('b', 'c')
graph.add_edge('b', 'd')
graph.add_edge('b', 'a')
graph.add_edge('c', 'd')
graph.add_edge('d', 'e')
graph.print_graph()
graph.remove_node('a')
print('after removal:')
graph.print_graph()
result = graph.find_cycle('b')
print(result)

#4