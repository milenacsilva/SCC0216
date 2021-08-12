from collections import defaultdict, deque

class Graph():
    ''' Defines a graph instance '''

    def __init__(self, adj_list=defaultdict(list)):
        self.adj_list = adj_list
        self.n = len(adj_list.keys())
    
    def init_pajek_graph(self, filename):
        ''' Reads a graph from a pajek formated file '''

        with open(filename, "r") as fp:
            self.amnt_vertices = int(fp.readline().split(" ")[1]) # Amount gets the amount of vertices
            fp.readline() # Unnecessary line

            while True:
                line = fp.readline().strip()
                if not line:
                    break
                
                ''' Gets all edges ''' 
                vertices = list(map(int, line.split(" ")))
                self.adj_list[vertices[0]].append(vertices[1]) 
                self.adj_list[vertices[1]].append(vertices[0])


        for i in range(1, self.amnt_vertices): # Initializes any unconnected vertices
            if i not in self.adj_list.keys():
                self.adj_list[i]
        self.n = len(self.adj_list)


    def bfs(self, start):
        ''' 
            Performs a bfs and returns the distance of each
            vertex to the starting vertex. 
        '''

        visited = [False] * (self.n + 1)
        dist = [-1] * (self.n + 1)

        queue = deque([start])
        visited[start] = True
        dist[start] = 0
        
        while queue:
            cur = queue.popleft() 
            neighbors = self.adj_list[cur] 
    
            for n in neighbors:
                if not visited[n]:
                    queue.append(n)
                    visited[n] = True  
                    dist[n] = dist[cur] + 1

                      
        return dist[1:] # Ignores the first index because vertices starts from 1 to n

    def get_dist_matrix(self):
        ''' Gets the distance matrix of a graph instance '''

        d_matrix = list()

        for i in range(1, self.n + 1):
            d_matrix.append(self.bfs(i))

        return d_matrix
        

def main():
    filename = input()
    filename.strip()

    graph = Graph()
    graph.init_pajek_graph(filename)
    
    d_matrix = graph.get_dist_matrix()
    for i in d_matrix: # Prints the distance matrix
        print(" ".join(map(str, i)))


main()