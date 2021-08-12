from collections import defaultdict

class Graph():
    ''' Defines a graph instance '''

    def __init__(self, adj_list=defaultdict(list)):
        self.amnt_vertices = len(adj_list.keys())
        self.adj_list = adj_list
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
        
    def get_connected_components(self):
        ''' Gets the amount of connected components of a graph and the amount of vertices each of them has'''

        amnt_labels, labeled_vertices = self._label_vertices()
        
        label_conter = [0] * amnt_labels
        for label in labeled_vertices:
            label_conter[label] += 1
        
        return amnt_labels, label_conter

    def _label_vertices(self):
        ''' Labels each connected vertice of a graph '''

        labeled_vertices = [-1] * (self.amnt_vertices + 1)
        label = 0

        for i in range(1, self.amnt_vertices):
            if labeled_vertices[i] == -1:
                self._labeling_dfs(labeled_vertices, i, label)
                label += 1
        
        # Ignores index 0, since pajek graph starts at 1
        return label, labeled_vertices[1:]

    def _labeling_dfs(self, labeled_vertices, start, label):
        ''' Dfs algorithm that labels the connected components of a graph '''
        stack = [start]
        labeled_vertices[start] = label
        
        while stack:
            cur = stack.pop() 
            neighbors = self.adj_list[cur] 
    
            for n in neighbors:
                if not labeled_vertices[n] != -1:
                    stack.append(n)
                    labeled_vertices[n] = label  
          

def main():
    filename = input()
    filename.strip()

    graph = Graph()
    graph.init_pajek_graph(filename)

    amnt_labels, label_conter = graph.get_connected_components()
    print(amnt_labels)
    
    # Sorts and prints the amount of vertices in each component
    label_conter.sort(reverse=True)
    for l in label_conter:
        print(l) 

main()