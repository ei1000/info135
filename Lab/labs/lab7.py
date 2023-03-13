#1


#2-3

class Graph:
    def __init__(self) -> None:
        self.graph = dict()
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

    def print_graph(self):
        print(self.graph)

graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'A')
graph.add_edge('C', 'A')
graph.add_edge('B', 'C')
graph.add_edge('F', 'B')

graph.print_graph()

#graph.nodes_out_degree(2)
print(graph.check_neighboor('F', 'B'))
graph.remove_edge('F', 'B')

graph.print_graph()

#graph.breadth_first_search('A')

#graph.print_graph()