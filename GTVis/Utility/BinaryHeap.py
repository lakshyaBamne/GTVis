class BinaryHeap:
    """
        Class to implement a priority queue structure used for efficient access
    """

    def __init__(self, *args, **kwargs):
        """
            Constructor takes as input an array and converts it to a heap
        """

        if len(args) != 0:
            
            # initialize some heap variables
            self.HEAP = args[0] # internally stored array
            self.N = len(args[0]) # length of the internal array
            self.LAST_PARENT = (self.N-2)//2 # last node in the heap that has atleast one child

            if kwargs["MIN"]: # min heap
                self.min_heapify()

                print("---Initialized a min heap on the input array---")
            else: # max heap
                self.max_heapify()

                print("---Initialized a max heap on the input array---")

        else:
            # Initialize an empty heap
            self.HEAP = []
            self.N = 0
            self.LAST_PARENT = 0

            if kwargs["MIN"]:
                print(f"---Initialized an empty min heap---")
            else:
                print(f"---Initialized an empty max heap---")

    #! Methods common to both min and max heap
    def left_child(self, i: int) -> int:
        """
            Method to get the left child of a node in a heap
        """
        return 2*i+1
    
    def right_child(self, i: int) -> int:
        """
            Method to get the right child of a node in a heap
        """
        return 2*i+2

    #! MIN-HEAP
    def is_min_heap(self, heap: list) -> bool:
        """
            Method to check if a given list is a binary min heap
        """
        N = len(heap)
        LAST_PARENT = (N-2)//2

        for i in  range(LAST_PARENT+1):
            lc = self.left_child(i)
            rc = self.right_child(i)

            if rc >= N:
                if heap[i] > heap[lc]:
                    return False
            else:
                if heap[i] > min(heap[lc] , heap[rc]):
                    return False
            
        return True

    def min_heapify(self):
        """
            Method to convert the given array to a min heap
        """

        for n in range(self.LAST_PARENT, -1, -1): # min heapify every node starting from the last parent
            self.min_heapify_node(n)
            

    def min_heapify_node(self, n: int) -> None:
        """
            Method to heapify a single node
        """

        print(f"---running heapify on node = {n}---") # log

        # do nothing if we have a leaf node
        if n > self.LAST_PARENT:
            return

        lc = self.left_child(n)
        rc = self.right_child(n)

        if rc >= self.N:
            # there is only one child
            if self.HEAP[n] > self.HEAP[lc]:
                print(f"swap[{n},{lc}]") # log

                self.HEAP[n], self.HEAP[lc] = self.HEAP[lc], self.HEAP[n]
                self.min_heapify_node(lc)
        else:
            # there are both children for this node
            if self.HEAP[n] > min(self.HEAP[lc],self.HEAP[rc]):

                # swap with left node and recursively heapify the left child
                if self.HEAP[lc] <= self.HEAP[rc]:
                    print(f"swap[{n},{lc}]") # log

                    self.HEAP[n], self.HEAP[lc] = self.HEAP[lc], self.HEAP[n]
                    self.min_heapify_node(lc)

                # swap with right node and recursively heapify the right child
                else:
                    print(f"swap[{n},{rc}]") # log

                    self.HEAP[n], self.HEAP[rc] = self.HEAP[rc], self.HEAP[n]
                    self.min_heapify_node(rc)

    def insert_to_min(self, value: int) -> None:
        """
            Method to insert an element to the min heap
        """

        # append the element at the end of the list
        self.HEAP.append(value)
        self.N += 1
        self.LAST_PARENT = (self.N-2)//2

        # now run the min heapify algorithm
        self.min_heapify()

        print(f"---Inserted {value} to the min heap---")

    def extract_from_min(self) -> int:
        """
            Method to remove and return the element at the top of the binary min heap
        """

        top = self.HEAP.pop(0)

        self.N = len(self.HEAP)
        self.LAST_PARENT = (self.N-2)//2

        print(f"---Extracted element from min heap -> {top}---")

        return top

    #! MAX-HEAP

    