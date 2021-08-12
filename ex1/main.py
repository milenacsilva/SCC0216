from random import random

def random_dissimilarity_matrix(n, parameter):
    ''' Generates a random matrix given probability `parameter` '''

    random_matrix = [[0]*n for i in range(0, n)]

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue

            pair_probability = random()
            if pair_probability > parameter:
                random_matrix[i][j] = 1
                random_matrix[j][i] = 1

    return random_matrix

def get_vertix_adjacency_list(matrix, vertex):
    ''' Gets the list of adjacent vertices of a given `vertex` '''
    
    adjacency_list = list()
    try:
        for v, i in enumerate(matrix[vertex]):
            if i == 1:
                adjacency_list.append(v)
        return adjacency_list
    except IndexError: # In case an invalid `vertex` is given
        print("Vértice inválido") 

def get_vertix_degree(matrix, vertex):
    ''' Gets the degree of a `vertex` '''

    try:
        return sum(matrix[vertex])
    except IndexError: # In case an invalid `vertex` is given
        print("Vértice inválido")

def is_adjacent(matrix, v_1, v_2):
    ''' Verifies if two branches are adjacent '''

    try:
        if matrix[v_1][v_2] == 1 and matrix[v_2][v_1] == 1:
            return True
        return False
    except IndexError: # In case invalid vertices are given
        print("Vértice inválido")

def print_matrix(matrix):
    ''' Prints a matrix by its rows '''

    top = ' '.join(map(str, [x for x in range(0, len(matrix))]))
    print(f"    {top}")
    print(f"  +-{len(top)*'-'}")

    for i, row in enumerate(matrix):
        print(f"{i} | {' '.join(map(str, row))}")

def main():
    
    r_matrix = random_dissimilarity_matrix(6, 0.7) 
    
    print("Matrix de adjacência:")
    print_matrix(r_matrix)
    print()

    print(f"Lista de adjacencia do vertice 2 ----> {get_vertix_adjacency_list(r_matrix, 2)}")
    print(f"Grau do vertice 4 ----> {get_vertix_degree(r_matrix, 4)}")
    print(f"0 e 5 são adjacentes? {is_adjacent(r_matrix, 0, 5)}")

if __name__ == '__main__':
    main()