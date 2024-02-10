class Graph:
    """
        Class represents a graph on which different operations can be performed
    """

    def __init__(self, **kwargs):
        """
            Constructor for the graph
        """
        # if user provides a path, read a graph from the given path
        if "PATH" in kwargs.keys():
            # get the adjacency list
            self.adj_list = self.read_graph(kwargs["PATH"])        
            
            # also initialize other variables for the graph
            self.initialize_graph_variables()

    def __str__(self) -> str:
        adj_list_repr = "ADJACENCY-LIST:\n"
        for n in range(len(self.adj_list)):
            adj_list_repr = adj_list_repr+ f"{n} -> " + str(self.adj_list[n]) + "\n"

        adj_matrix_repr = "ADJACENCY-MATRIX\n"
        for row in self.adj_matrix:
            adj_matrix_repr = adj_matrix_repr + str(row) + "\n"

        str_repr = f"---Undirected Unweighted Graph---\n{adj_list_repr}\n{adj_matrix_repr}---"
        
        return str_repr

    def read_graph(self, path: str) -> list[list]:
        """
            Method to read a graph from an external file
            returns the adjacency list representation of the graph

            -> assumes that the external file also contains an adjacency list
            -> delimiter should be a comma
        """
        # adjacency list for the graph
        graph = []

        # read all lines from the external file
        with open(path, "r") as f:
            nodes = f.readlines()

        for node in nodes:
            graph.append( list(map(int, node.split(",")[:-1])) )

        return graph

    def list_to_matrix(self, adj_list: list[list]) -> list[list]:
        """
            Method to convert a given adjacency list to an adjacency matrix
        """

        # get the number of nodes in the graph
        n = len(adj_list)

        # make an empty nxn matrix
        matrix = [[0 for i in range(n)] for j in range(n)]

        # add the edges which are present in the list
        for i in range(n):
            for node in adj_list[i]:
                matrix[i][node] = 1

        return  matrix

    def initialize_graph_variables(self) -> None:
        """
            Method to initialize all the variables for the graph
            -> works only when the object already has an adjacency list representation
        """

        # first convert and store an adjacency matrix representation of the
        # graph as well for later usage
        self.adj_matrix = self.list_to_matrix(self.adj_list)

        # number of nodes
        self.N = len(self.adj_list)