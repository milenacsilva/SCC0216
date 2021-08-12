from random import random

def r_dissimilarity_matrix(n, parameter):
    r_matrix = [[0]*n for i in range(0, n)]

    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                continue

            pair_probability = random()
            if pair_probability > parameter:
                r_matrix[i][j] = 1

    return r_matrix

def dissimilarity_matrix_to_csv(n, matrix):
    out_file = str(input("Name of the ouput file: "))
    
    with open(out_file, "w") as of:
        of.write("Source,Target,Type,weight\n")
        for i in range(0, n):
            point_written = False
            for j in range(0, n):
                if matrix[i][j]:
                    point_written = True
                    of.write(f"{i},{j},Directed,1\n")
            
            if not point_written:
                of.write(f"{i},{i},Directed,1\n")

matrix = r_dissimilarity_matrix(4, 0.5)
print(matrix)
dissimilarity_matrix_to_csv(4, matrix)
