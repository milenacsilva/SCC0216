from collections import defaultdict

class Graph():
    ''' Defines a graph instance '''

    def __init__(self, adj_list=defaultdict(list)):
        self.amnt_vertices = len(adj_list.keys())
        self.adj_list = adj_list
        self.labeled_vertices = None
        self.amnt_components = 0
    
    def init_pajek_graph(self, filename):
        ''' Reads a graph from a pajek formated file '''

        with open(filename, "r") as fp:
            self.amnt_vertices = int(fp.readline().split(" ")[1]) # Amount gets the amount of vertices
            type = fp.readline() # Unnecessary line

            while True:
                line = fp.readline().strip()
                if not line:
                    break
                
                # Gets edges/arcs 
                vertices = list(map(int, line.split(" ")))
                self.adj_list[vertices[0]].append(vertices[1]) 
                
                # Type can be `*Edges` or `*Arcs` depending if is a directed or undirected graph
                if type == "*Edges\n": 
                    self.adj_list[vertices[1]].append(vertices[0])


        for i in range(1, self.amnt_vertices): # Initializes any unconnected vertices
            if i not in self.adj_list.keys():
                self.adj_list[i]

    def has_cycle(self):
        ''' Verifies if a directed graph has a cycle by using a dfs algorithm'''
        
        visited = [False] * (self.amnt_vertices + 1)
        
        stack = [1]
        visited[1] = True

        while stack:
            cur = stack.pop() 
            neighbors = self.adj_list[cur] 
    
            for n in neighbors:
                if not visited[n]:
                    stack.append(n)
                else:
                    return True
        
        return False
    

def main():
    filename = input()
    filename.strip()

    graph = Graph()
    graph.init_pajek_graph(filename)

    print("S" if graph.has_cycle() else "N")

main()