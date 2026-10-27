# DSA Day 55 - Backtracking (Part 3)

## Topics Covered

1. Generate Parentheses using Backtracking
2. Generate and Store Valid Parentheses Combinations
3. Generate Combinations of Size K from an Array

## Programs

### 1. Generate Parentheses - Print Results
- Generates all valid combinations of n pairs of parentheses.
- Uses opening and closing count conditions.
- Prints each valid combination.

### 2. Generate Parentheses - Store Results
- Generates all valid parentheses combinations.
- Stores the results in a list.
- Returns the complete list of combinations.

### 3. Combinations of Size K
- Generates all combinations of size k from an array.
- Uses recursion, a loop, and backtracking.
- Adds an element, explores the next choices, and removes the element.

## Key Concepts

- Recursion
- Backtracking
- Base Case
- Choosing and Exploring
- Undoing a Choice
- Valid Parentheses Conditions
- Generating Combinations

## Complexity

### Generate Parentheses
- Time Complexity: O(Cn * n), where Cn is the nth Catalan number.
- Space Complexity: O(n) auxiliary recursion depth, excluding output storage.

### Combinations of Size K
- Number of Combinations: C(n, k)
- Time Complexity: O(k * C(n, k)) for generating and storing combinations.
- Space Complexity: O(k) auxiliary space, excluding stored output.

