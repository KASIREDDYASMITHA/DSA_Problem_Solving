
# DSA Day 62 - Dynamic Programming 1

## Topics Covered

- Introduction to Dynamic Programming (DP)
- Fibonacci using Recursion
- Overlapping Subproblems
- Top-Down Dynamic Programming (Memoization)
- Bottom-Up Dynamic Programming (Tabulation)

## Learning Summary

Dynamic Programming is an optimization technique in which we calculate a function value once, store the result, and reuse it whenever required.

### Approaches

1. Recursion - Solving a problem by calling the same function with smaller inputs.
2. Top-Down DP - Recursion with memoization (storing calculated results).
3. Bottom-Up DP - Iteratively calculating and storing results in a DP array.

## Fibonacci Problem

The Fibonacci sequence is:

0, 1, 1, 2, 3, 5, 8, 13, 21, ...

Formula:

fib(n) = fib(n-1) + fib(n-2)

Base Conditions:

- fib(0) = 0
- fib(1) = 1

## Python Programs

1. fibonacci_recursion.py
2. fibonacci_top_down.py
3. fibonacci_bottom_up.py

## Problem-Solving Flow

1. Understand the problem statement.
2. Write the recursive solution.
3. Convert the recursive solution into Top-Down DP.
4. Convert the Top-Down DP solution into Bottom-Up DP.

## Key Takeaway

Dynamic Programming avoids repeated calculations by storing and reusing previously computed results.
