# DSA Day 21 - Majority Element

## Topic: Majority Element

A majority element is an element that occurs more than `n/2` times in an array.

### Important Note

At most one majority element can exist in an array.

For example:

```text
Array: 2 2 1 2 3 2 2

n = 7
n/2 = 3.5

2 occurs 5 times.

5 > 3.5

Therefore, 2 is the Majority Element.
```

---

# Approach 1: Brute Force

In the Brute Force approach, compare every element with every other element and count how many times each element occurs.

If the count of an element is greater than `n/2`, that element is the majority element.

### Steps

1. Read the array.
2. Find the size of the array `n`.
3. Take every element one by one.
4. Count its occurrences using another loop.
5. Check whether the count is greater than `n/2`.
6. If true, print the majority element.
7. If no element satisfies the condition, print `-1`.

### Time Complexity

```text
O(n²)
```

### Space Complexity

```text
O(1)
```

---

# Approach 2: HashMap

In the HashMap approach, store the frequency of every element.

The key represents the array element and the value represents its frequency.

### Steps

1. Read the array.
2. Create an empty HashMap.
3. Count the frequency of every element.
4. Traverse the frequency table.
5. Check whether any frequency is greater than `n/2`.
6. Print that element.
7. If no element satisfies the condition, print `-1`.

### Important Point

If there are no duplicate elements in the input array, the number of entries in the HashMap will be equal to the size of the array `n`.

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(n)
```

---

# Approach 3: Sorting

In the Sorting approach, first sort the array.

After sorting, a majority element, if present, must occupy the middle position or cross the middle position.

We can check whether the element at position `i` is equal to the element at `i + n//2`.

### Steps

1. Read the array.
2. Sort the array.
3. Find the size `n`.
4. Compare elements separated by `n//2`.
5. If the same element is found, it is the majority element.
6. Otherwise, print `-1`.

### Time Complexity

```text
O(n log n)
```

### Space Complexity

```text
O(1)
```

---

# Approach 4: Boyer-Moore Voting Algorithm

The Boyer-Moore Voting Algorithm finds a possible majority element using a candidate and a count.

### Variables

```text
candidate
count
```

### Steps

1. Initialize `count = 0`.
2. Traverse the array.
3. If `count == 0`, make the current element the candidate.
4. If the current element is equal to the candidate, increase `count`.
5. Otherwise, decrease `count`.
6. After the loop, the candidate is a possible majority element.
7. Verify the candidate by counting its occurrences.
8. If its frequency is greater than `n/2`, return the candidate.
9. Otherwise, return `-1`.

### Time Complexity

```text
O(n)
```

### Space Complexity

```text
O(1)
```

---

# Comparison of Approaches

| Approach    | Time Complexity | Space Complexity |
| ----------- | --------------: | ---------------: |
| Brute Force |           O(n²) |             O(1) |
| HashMap     |            O(n) |             O(n) |
| Sorting     |      O(n log n) |             O(1) |
| Boyer-Moore |            O(n) |             O(1) |

## Conclusion

The Majority Element problem can be solved using different approaches.

The Boyer-Moore Voting Algorithm uses a candidate and count and then verifies the candidate to make sure it actually occurs more than `n/2` times.
