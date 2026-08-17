"""
DSA Day 9
Topic: Linear Search

Best Case  : O(1)
Worst Case : O(n)
"""


def linear_search(arr, key):
    """
    Searches for key in the array.

    Returns:
        Index of the key if found
        -1 if the key is not found
    """

    for i in range(len(arr)):

        if arr[i] == key:
            return i

    return -1


# --------------------------------------------------
# Main Program
# --------------------------------------------------

if __name__ == "__main__":

    arr = [2, 4, 11, 16, 9, 8]

    print("Array:", arr)

    # Best Case
    # Key is present at the first position.
    result = linear_search(arr, 2)

    print("\nBest Case:")
    print("Key: 2")
    print("Index:", result)
    print("Time Complexity: O(1)")

    # Average / General Case
    result = linear_search(arr, 11)

    print("\nGeneral Case:")
    print("Key: 11")
    print("Index:", result)

    # Worst Case
    # Key is present at the last position.
    result = linear_search(arr, 8)

    print("\nWorst Case:")
    print("Key: 8")
    print("Index:", result)
    print("Time Complexity: O(n)")

    # Worst Case
    # Key is not present.
    result = linear_search(arr, 100)

    print("\nKey Not Found:")
    print("Key: 100")
    print("Index:", result)
    print("Time Complexity: O(n)")