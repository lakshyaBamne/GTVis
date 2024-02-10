class Queue:
    """
        Class represents the queue data structure
        
        Main Attributes:
        -> length : number of elements in the Queue at any time

        Main operations:
        -> push : add an element to the Queue
        -> front : remove and return the element at the front of the queue
    """

    def __init__(self):
        """
            Constructor initializes an empty queue
        """

        # initialize a list to store the queue elements
        self.queue = []

    def __str__(self) -> str:
        return f"Queue(front-last) : {self.queue}"

    def insert(self, element: tuple[int]) -> None:
        """
            Insert an element to the Queue, each element is a tuple
        """

        # add the element at the end of the list
        self.queue.append(element)

    def front(self) -> tuple[int]:
        """
            Remove and return the element at the front of the Queue
        """

        # remove and return the element at the start of the list
        return self.queue.pop(0)

    def empty(self) -> bool:
        """
            Method to check if the Queue is empty or not
        """
        
        if len(self.queue) == 0:
            return True
        else:
            return False


