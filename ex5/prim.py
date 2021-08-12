from collections import OrderedDict
from queue import PriorityQueue


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

      
    def get_MST(self):        
        pqueue = PriorityQueue()

        parent = [-1] * (self.n + 1)
        key = [INFINITY] * (self.n + 1)
        inMST = [False] * (self.n + 1)

        key[1] = 0
        pqueue.put((key[1], 1))

        while not pqueue.empty():
            u = pqueue.get()[1]
            
            if inMST[u]:
                continue
            
            neighbors = self.adj_list[u]
            for pair in neighbors:
                if not inMST[pair.v] and key[pair.v] > pair.weight:
                    key[pair.v] = pair.weight
                    pqueue.put((key[pair.v],pair.v))
                    parent[pair.v] = u
            

            inMST[u] = True
        
        return key[1:]
            
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
            elif type == "*Edges\n":
                graph.add_edge(u=line[U], v=line[V], weight=line[WEIGHT])
    
    return graph

def main():
    filename = input()
    filename.strip()

    graph = init_pajek_graph(filename)
    print(graph.adj_list)

    # edges = graph.get_MST()
    # print(sum(edges))

main()