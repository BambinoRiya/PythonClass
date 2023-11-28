#-------------- Question 1 --------------

def adjacency_list_to_matrix(adj_list):
    num_vertices = len(adj_list)
    adj_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    
    for i in range(num_vertices):
        for j in adj_list[i]:
            adj_matrix[i][j] = 1

    return adj_matrix

# Test case
adj_list_sample = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

result_matrix = adjacency_list_to_matrix(adj_list_sample)
expected_result = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]

# Print the result for verification
print("Result:", result_matrix)
if result_matrix == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again")



#-------------- Question 2 --------------
    
def adjacency_matrix_to_adjacency_list(adj_matrix):
    adj_list = {}

    for i in range(len(adj_matrix)):
        adj_list[i] = []
      
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] != 0:
                adj_list[i].append(j)
    return adj_list

# Test case
adj_matrix_sample = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 1]
]

result_adj_list = adjacency_matrix_to_adjacency_list(adj_matrix_sample)
expected_result = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Print the result for verification
print("Result:", result_adj_list)
if result_adj_list == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again.")
    
#-------------- Question 3 --------------
    
def edge_list_to_adjacency_list(edge_list):
    adj_list = {}

    for edge in edge_list:
        # Unpack the tuple
        u, v = edge

        # If u is not in the adjacency list, add it with an empty list
        if u not in adj_list:
            adj_list[u] = []

        # Add v to the list of u's neighbors
        adj_list[u].append(v)

        # If v is not in the adjacency list, add it with an empty list
        # This is necessary for vertices that have no outgoing edges
        if v not in adj_list:
            adj_list[v] = []

    return adj_list

# Test case
edge_list_sample = [(0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3)]

result_adj_list = edge_list_to_adjacency_list(edge_list_sample)
expected_result = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

# Print the result for verification
print("Result:", result_adj_list)
if result_adj_list == expected_result:
    print("Correct! Your code produced the expected result.")
else:
    print("Incorrect! Please try again.")
