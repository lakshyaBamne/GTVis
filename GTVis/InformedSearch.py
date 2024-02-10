from GTVis.Graph import Graph
from GTVis.Utility.Queue import Queue
from GTVis.Utility.Stack import Stack

class InformedSearch(Graph):
    """
        Class to represent the informed search algorithms on the graph
        -> subclass of Graph
    """

    def __init__(self, **kwargs):
        """
            Constructor for the informed search algorithms
        """
        # if user provides a path, read a graph from the given path
        if "PATH" in kwargs.keys():
            # get the adjacency list
            self.adj_list = self.read_graph(kwargs["PATH"])        
            
            # also initialize other variables for the graph
            self.initialize_graph_variables()

        # initialize the dictionaries to store the informerd search results
        self.BFS_ORDER = {}
        self.DFS_ORDER = {}

    def BreadthFirstSearch(self, root: int) -> None:
        """
            Method to perform Breadth first search on the undirected un
            -> store the order and levels in a dictionary in the object
        """
        # list store the order in which the nodes are visited during BFS
        bfs_order = []

        # indicators for the nodes already visited
        # visited means we have arrived at the node and then look around it
        visited = [False for i in range(self.N)]

        # indicator to check if an element is already added to the queue
        # prevents adding the same node to the queue multiple times
        enqueue = [False for i in range(self.N)]

        # processing queue for BFS
        processing = Queue()

        # add the root to the queue and start the search algorithm
        # root is considered to be at the 0th level here
        processing.insert((root, 0))
        enqueue[root] = True

        while not processing.empty():
            # extract the element at the front of the queue to process
            to_process = processing.front()

            bfs_order.append(to_process)

            # get the node number and the level at which the node is present
            node = to_process[0]
            level = to_process[1]

            # mark the extracted node as visited
            visited[node] = True

            for neighbour in self.adj_list[node]:
                if not visited[neighbour] and not enqueue[neighbour]:
                    processing.insert((neighbour, level+1))
                    enqueue[neighbour] = True

        # initialize the variables associated with informed searches
        self.BFS_ORDER[f"{root}"] = bfs_order

    def DepthFirstSearch(self, root: int) -> None:
        """
            Method to perform Depth first search starting from the given root node
            -> store the order of 
        """

        # list to store the order in which nodes are visited during DFS
        dfs_order = []

        # indicator vector to check which nodes have already been visited
        visited = [False for i in range(self.N)]

        # indicator vector to check which nodes have been added to a stack already
        # this is to ensure same node is added twice
        enstack = [False for i in range(self.N)]

        # processing stack
        processing = Stack()

        # start by adding the root element to the stack
        processing.insert((root))

        while not processing.empty():
            # extract the element at the top of the stack
            to_process = processing.top()

            visited[to_process] = True

            dfs_order.append(to_process)

            for neighbour in self.adj_list[to_process]:
                if not visited[neighbour] and not enstack[neighbour]:
                    processing.insert((neighbour))
                    enstack[neighbour] = True
                
        # initialize the DFS order to a dictionary in the object
        self.DFS_ORDER[f"{root}"] = dfs_order