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
    if len(arr) <= 0:
        return "Array is empty."
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
    if len(arr) <= 0:
        return "Array is empty."
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
    if len(arr) <= 0:
        return "Array is empty."
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
- Quick sort is implemented by assigning a pivot (often the element at the end of the array).
- Elements are then partitioned around the pivot (greater than or less than).
"""


def partition(arr, low, high):
    i = low - 1  # Index of smaller element
    pivot = arr[high]  # Pivot the element at the end of the array
    for j in range(low, high):
        if arr[j] <= pivot:  # Is the element greater or less?
            i = i + 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = (
        arr[high],
        arr[i + 1],
    )  #  If GT, swap greater value with pivot
    return i + 1  #  Return the index


def quickSort(arr, low, high):
    """
    arr (list): Array to be sorted
    low (int):  Start index
    high (int): End index
    """
    if len(arr) == 0:
        return "Array is empty."
    elif len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)  #  Assign the partitioning index
        quickSort(
            arr, low, pi - 1
        )  # Recursively call 'quickSort' to sort elements before partition
        quickSort(
            arr, pi + 1, high
        )  # Recursively call 'quickSort' to sort elements after partition


x = [6, 3, 8, 50]
xLen = len(x)
quickSort(x, 0, xLen - 1)
print(x)  # Output: [3, 6, 8, 50]

"""
H E A P   S O R T
"""
"""
- Similar to selection sort, the maximum element is placed at the end.
- Within a heap, the first node will always be the largest. Array[0].
- Every parent node will be greater than it's child.
- The heap is generated from left to right.
"""


def buildHeap(arr, n, i):
    largest = i  # Select the first node
    l = 2 * i + 1  # As index = 0, left child node
    r = 2 * i + 2  # As index = 0, right child node
    if (
        l < n and arr[largest] < arr[l]
    ):  # Does left child exist and is it greater than root
        largest = l
    if (
        r < n and arr[largest] < arr[r]
    ):  # Does right child exist and is greater than root
        largest = r
    if largest != i:  # Change root, if needed
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap if needed
        buildHeap(arr, n, largest)  # buildHeap the root


def heapSort(arr):
    n = len(arr)
    if n == 0:
        return "Array is empty."
    elif n == 1:
        return arr
    for i in range(n // 2 - 1, -1, -1):  # Build a maxheap
        buildHeap(arr, n, i)
    for i in range(n - 1, 0, -1):  # One by one extract elements
        arr[i], arr[0] = arr[0], arr[i]  # Swap elements
        buildHeap(arr, i, 0)


x = [12, 11, 240, 5, -66, 7, -2]
heapSort(x)
print(x)  # Output: [-66, -2, 5, 7, 11, 12, 240]

"""
M E R G E   S O R T
"""
"""
- Similar to quick sort, merge sort partitions the array in two.
- Partitions are then sorted before being merged back resulting in a single sorted array.
"""


def mergeSort(arr):
    if len(arr) == 0:
        return "Array is empty."
    elif len(arr) == 1:
        return arr
    else:
        mid = len(arr) // 2  #  Locate the middle of the array
        L = arr[:mid]  #  Split the array into 'L' and 'R'
        R = arr[mid:]
        mergeSort(L)  # Sort the left
        mergeSort(R)  # Sort the right
        i = j = k = 0
        while i < len(L) and j < len(R):  # Copy data to temp arrays 'L' and 'R'
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):  #  Check for remaining elements
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def printList(arr):
    outputArr = []
    for i in range(len(arr)):
        outputArr.append(arr[i])
    print(outputArr)


x = [6, 300, 8, 50, -2]
mergeSort(x)
printList(x)  # Output: [-2, 6, 8, 50, 300]