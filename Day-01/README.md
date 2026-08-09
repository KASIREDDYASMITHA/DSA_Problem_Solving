# Day 01 - Flowcharts and Conditional Statements

## Topics Covered

- Flowcharts
- Standard flowchart symbols
- Sequence
- Selection
- if, elif and else
- Conditional reasoning
- Modulo operator
- Short-circuiting
- Output tracing
- Basic conditional programming in Python

---

## Flowchart

A flowchart is a diagram that represents the steps of an algorithm using standard geometric shapes connected by arrows.

### Standard Flowchart Symbols

| Symbol | Name | Purpose |
|---|---|---|
| Rounded Rectangle | Terminal | Start / Stop |
| Rectangle | Process | Action or computation |
| Diamond | Decision | Branch based on a condition |
| Parallelogram | Input / Output | Read input or display output |
| Circle | Connector | Connect different parts of a flowchart |
| Arrow | Flow Line | Shows the direction of flow |

---

## Types of Flowcharts

### 1. Sequence

Steps are executed one after another in a fixed order.

Example:

Start → Step A → Step B → Step C → Stop

There is no branching or repetition.

### 2. Selection

A condition is tested and the program follows a branch based on whether the condition is true or false.

Example:

```text
        Condition?
        /        \
      Yes        No
       |          |
    If block   Else block
       \          /
          Stop