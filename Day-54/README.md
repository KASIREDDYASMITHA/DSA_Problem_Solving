# DSA Day 54 - Backtracking - 2

## Topics Covered
- Backtracking general template
- State in recursion
- Generating permutations of a string
- Generating binary strings using recursion
- Recursive calls and base conditions
- String concatenation

## 1. Backtracking

Backtracking is a problem-solving technique that explores different possible choices using recursion.

At each step:
1. Check whether the solution is complete.
2. If complete, record or print the solution and return.
3. Consider the available choices.
4. Skip invalid choices.
5. Make a choice.
6. Recursively explore the new state.
7. Undo the choice when necessary.

### General Template

```text
backtrack(state):
    if solution is complete:
        record solution
        return

    for each choice:
        if choice is invalid:
            continue

        choose(choice)
        backtrack(new_state)
        undo(choice)