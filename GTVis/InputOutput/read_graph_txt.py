"""
    Module to help read an adjacency list from a text file
"""

def read_adj_list_txt(path: str, delimiter: str) -> list[list]:
    """
        Function to read a text file and load the stored
        adjacency list in it

        @path : path of the file relative to the main python script
        @delimiter : delimiter used to separate nodes in the txt file
    """

    with open(path, "r") as f:
        lines = f.readlines()

    adj_list = []

    for line in lines:
        adj_list.append( list(map(int, line.split(delimiter)[:-1])) )

    return adj_list

def read_adj_matrix_txt(path: str, delimiter: str) -> list[list]:
    """
        Function to read a text file and load the stored adjacency matrix

        @path : path of the file relative to the main python script
        @delimiter : delimiter used to separate nodes in the txt file
    """

    with open(path, "r") as f:
        lines = f.readlines()

    adj_matrix = []

    for line in lines:
        row = []
        for i in line.split(delimiter)[:-1]:
            if i != "n":
                row.append( int(i) )
            else:
                row.append(None)
        adj_matrix.append(row)

    return adj_matrix