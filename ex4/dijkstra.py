from collections import OrderedDict
from os import P_PGID

INFINITY = 100000000000
U, V, WEIGHT = range(3)

class Arc():
    def __init__(self, v, weight=1):
        self.v = v
        self.weight = weight



class Graph():
    ''' Defines a graph instance '''

    def __init__(self, n):
        self.n = n
        self.adj_list = OrderedDict([(x + 1, list()) for x in range(0, n)])

    def add_arc(self, u, v, weight):
        self.adj_list[u].append(Arc(v=v, weight=weight))

    def add_edge(self, u, v, weight):
        self.adj_list[u].append(Arc(v=v, weight=weight))
        self.adj_list[v].append(Arc(v=u, weight=weight))

    def _min_dis(self, unvisited, distance):      
        u_min = -1
        min_dis = INFINITY 

        for u in unvisited:
            if distance[u] < min_dis:
                u_min = u
                min_dis = distance[u]

        return u_min, min_dis

    def dijkstra(self, start):
        distance = [INFINITY] * (self.n + 1)
        distance[start] = 0
        
        unvisited = list(self.adj_list.keys())
        visited = []

        while unvisited:
            u_min, min_dis = self._min_dis(unvisited, distance)
            neighbors = self.adj_list[u_min]

            for n in neighbors:
                new_dis = min_dis + n.weight

                if new_dis < distance[n.v]:
                    distance[n.v] = new_dis

            unvisited.remove(u_min)
            visited.append(u_min)

        return distance[1:]
            
    def get_min_distance_matrix(self):
        matrix = list()
        
        for u in self.adj_list.keys():
            matrix.append(self.dijkstra(u))

        return matrix

def init_pajek_graph(filename):
    ''' Reads a graph from a pajek formated file '''
    graph = None
    with open(filename, "r") as fp:
        # Initializes the graph
        n = int(fp.readline().split(" ")[1]) 
        type = fp.readline() 
        graph = Graph(n=n)
        
        while True:
            line = fp.readline().strip()
           
            if not line:
                break
            
            line = list(map(int, line.split(" ")))
            
            if type == "*Arcs\n":
                graph.add_arc(u=line[U], v=line[V], weight=line[WEIGHT])
    
    return graph

def print_matrix_with_padding(matrix):
    max_padding = len(str(max(map(max, matrix))))

    for i in matrix:
        print(" ".join([f"{x:{len(str(max(max(matrix))))}}" for x in i]))

def main():
    filename = input()
    filename.strip()

    graph = init_pajek_graph(filename)

    matrix = graph.get_min_distance_matrix()
    print_matrix_with_padding(matrix)

main()