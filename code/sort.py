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
- The algorithm starts left to right examining each item by comparing to items on it's left.
- Less efficient when dealing with large arrays.
"""


def insertionSort(arr):
    for i in range(1, len(arr)):  # Traverse through array (exclude first element)
        key = arr[i]
        j = i - 1  # Select element to the left
        while j >= 0 and key < arr[j]:  # While the element is less than the key
            arr[j + 1] = arr[j]  # Swap the elements over, smallest first
            j -= 1  # When -1 is reach, this is the end of the array
        arr[j + 1] = key  # Set the next element as the key
    print(arr)


x = [6, 3, 8]
insertionSort(x)  # Output: [3, 6, 8]

"""
S E L E C T I O N   S O R T
"""
"""
- Elements are sorted by repeatedly finding the minimum element in the array.
- Once the smallest element is located, it is swapped with the current idx.
- Each iteration results in another sorted element.
- This algorithm works well on smaller arrays but time complexity can be O(N^2).
"""


def selectionSort(arr):
    for i in range(len(arr)):  # Traverse through all array elements
        min_idx = i  # Find the minimum element in remaining unsorted array
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = (
            arr[min_idx],
            arr[i],
        )  # Swap the found minimum element with the first element
    print(arr)


x = [5, 10, 120, 22, 11]
selectionSort(x)  # Output: [5, 10, 11, 22, 120]


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