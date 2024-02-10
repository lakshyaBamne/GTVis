class Stack:
    """
        Class represents the stack data structure
        
        Main Attributes:
        -> length : number of elements in the Queue at any time

        Main operations:
        -> push : add an element to the stack
        -> pop : remove and return the element at the top of the stack
    """

    def __init__(self):
        """
            Constructor initializes an empty queue
        """

        # initialize a list to store the queue elements
        self.stack = []

    def __str__(self) -> str:
        return f"Stack(top-bottom) : {self.stack[::-1]}"

    def insert(self, element: tuple[int]) -> None:
        """
            Insert an element to the Queue, each element is a tuple
        """

        # add the element at the end of the list
        self.stack.append(element)

    def top(self) -> tuple[int]:
        """
            Remove and return the element at the front of the Queue
        """

        # remove and return the element at the start of the list
        return self.stack.pop(-1)

    def empty(self) -> bool:
        """
            Method to check if the Queue is empty or not
        """
        
        if len(self.stack) == 0:
            return True
        else:
            return False


