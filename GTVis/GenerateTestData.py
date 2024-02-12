"""
    Module contains some functions to generate random test data
"""
import random
import numpy as np
import math

def generate_random_integers(n: int, a: int, b: int, **kwargs) -> list:
    """
        Function to generate a random list of integers in a range
    """

    nums = [random.randrange(a, b) for _ in range(n)]
    random.shuffle(nums) # shuffle the array once for more randomness

    if "PATH" in kwargs.keys():
        with open(kwargs["PATH"], "w") as f:
            f.write(str(nums))

    return nums

