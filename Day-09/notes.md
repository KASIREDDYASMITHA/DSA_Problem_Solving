
# DSA Day 9 — Time and Space Complexity

## 1. Time Complexity

Time complexity is used to measure how the running time or number of operations of an algorithm grows as the input size increases.

We study time complexity so that we can compare algorithms based on their efficiency instead of depending only on the actual execution time on a particular computer.

---

## 2. Space Complexity

Space complexity describes how much memory an algorithm requires as the input size increases.

### Time Complexity

Measures the growth of operations/time.

### Space Complexity

Measures the growth of memory usage.

---

# 3. Why Do We Need Time and Space Complexity?

Two algorithms may solve the same problem but may use different amounts of time and memory.

Therefore, we analyze algorithms to determine which solution is more efficient.

Actual execution time can depend on:

- Processor
- RAM
- Programming language
- Compiler
- Operating system
- System environment

Because of this, we use mathematical analysis to compare algorithms.

---

# 4. Apriori Analysis

Apriori Analysis is the analysis of an algorithm **before executing the program**.

It uses a mathematical model to analyze the efficiency of an algorithm based on the number of operations.

### Advantages

- Does not depend on a particular machine.
- Does not require executing the program.
- Helps compare algorithms.
- Gives an idea about the growth of an algorithm.

---

# 5. Posteriori Analysis

Posteriori Analysis is the analysis of an algorithm **after executing the program**.

It measures the actual performance of the program.

It can depend on:

- Processor speed
- RAM
- Programming language
- Compiler
- Operating system
- System load
- Execution environment

---

# 6. Asymptotic Analysis

Asymptotic analysis studies how the running time of an algorithm grows when the input size becomes large.

The main focus is on the **growth rate** rather than the exact execution time.

For example:

```text
T(n) = 3n² + 5n + 10