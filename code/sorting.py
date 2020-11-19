"""
S O R T I N G   I N   P Y T H O N
"""
"""
B U B B L E   S O R T
"""
"""
- Bubble sort is the simplest sorting algorithm.
- Adjacent elements are swapped if the right element is larger than the left.
"""


def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):  # Traverse through array
        for j in range(0, n - i - 1):  # Last i elements already in place
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = (
                    arr[j + 1],
                    arr[j],
                )  # If condition is met, swap elements
    print(arr)


x = [1, 4, 3, 5, -6, 2]
bubbleSort(x)  # Output: [-6, 1, 2, 3, 4, 5]

"""
I N S E R T I O N   S O R T
"""
"""
- Insertion sort is implemented one element at a time.
- Less efficient when dealing with large arrays.
"""


def insertionSort(arr):
    for i in range(1, len(arr)):  # Traverse through array (exclude first element)
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    print(arr)


x = [6, 3, 8]
insertionSort(x)  # Output: [3, 6, 8]

"""
S E L E C T I O N   S O R T
"""
"""
- 
"""


"""
T H R E E   N U M B E R   S O R T
"""
"""
- 
"""


"""
Q U I C K  S O R T
"""
"""
- 
"""


"""
H E A P   S O R T
"""
"""
- 
"""


"""
M E R G E   S O R T
"""
"""
- 
"""