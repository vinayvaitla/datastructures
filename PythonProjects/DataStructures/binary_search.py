"""
Program to perform Binary Search on an Array using ADT to store and retrieve Elements.
1. Array should be in the Sorted Fashion
2. Time Complexity is
   Best Case - O(1)
   Worst Case - O(logn)
   Average Case - O(logn)
"""
from lib.singlearray import SingleArray


def binary_search(value):
    """
    This method searches the value in the array provided the data in the array is sorted.
    Uses Binary Search Algorithm
    :param value:
    :return position:
    """
    low = 0
    high = sa.get_used_size()
    while low <= high:
        mid = int((low+high)/2)
        if value < sa.data[mid]:
            high = mid-1
        elif value > sa.data[mid]:
            low = mid+1
        else:
            return mid+1
    return -1

# Instantiating an Object to create an Array
sa = SingleArray(10)

# Set values to the Array
sa.set_value(5)
sa.set_value(9)
sa.set_value(11)
sa.set_value(17)
sa.set_value(20)
sa.set_value(45)
sa.set_value(78)
sa.set_value(99)

# Displays Array Information
sa.print_array()

# Executing Binary Search
result_position = binary_search(45)
if result_position != -1:
    print (f"Element found at {result_position}")
else:
    print("Element not found!")
