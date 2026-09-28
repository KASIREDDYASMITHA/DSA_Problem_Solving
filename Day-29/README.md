# DSA Day 29 – Stack
## Infix, Prefix, Postfix and Evaluate Reverse Polish Notation

## 1. Expression Notations

Expression notation defines how operators and operands are arranged in an expression.

There are three types of expression notations:

1. Infix Notation
2. Prefix Notation (Polish Notation)
3. Postfix Notation (Reverse Polish Notation)

---

## 2. Infix Notation

### Definition
In infix notation, the operator is written between the operands.

It is the notation commonly used in mathematics.

### Examples

- A + B
- A * B
- (A + B) * C

### Characteristics

- The operator is written between the operands.
- Operator precedence is required.
- Parentheses can be used to specify the order of operations.
- Computers need additional rules to evaluate infix expressions.

### Example

Expression: (A + B) * C

Here:
- First, A and B are added.
- Then, the result is multiplied by C.

---

## 3. Prefix Notation (Polish Notation)

### Definition
In prefix notation, the operator is written before the operands.

### Examples

Infix: A + B
Prefix: + A B

Infix: (A + B) * C
Prefix: * + A B C

### Characteristics

- The operator is written before the operands.
- Parentheses are not required.
- Operator precedence rules are not required.
- Evaluation is typically performed from right to left using a stack.

### Example

Infix: (A + B) * C

Prefix: * + A B C

The expression means:
1. Add A and B.
2. Multiply the result by C.

---

## 4. Postfix Notation (Reverse Polish Notation)

### Definition
In postfix notation, the operator is written after the operands.

Postfix notation is also called Reverse Polish Notation (RPN).

### Examples

Infix: A + B
Postfix: A B +

Infix: (A + B) * C
Postfix: A B + C *

### Characteristics

- The operator is written after the operands.
- Parentheses are not required.
- Operator precedence rules are not required.
- Evaluation is performed from left to right using a stack.

### Example

Infix: (A + B) * C

Postfix: A B + C *

The expression means:
1. Add A and B.
2. Multiply the result by C.

---

## 5. Difference Between Infix, Prefix and Postfix

| Notation | Operator Position | Example |
|----------|-------------------|---------|
| Infix | Between operands | A + B |
| Prefix | Before operands | + A B |
| Postfix | After operands | A B + |

### Example Using All Three Notations

Expression: (A + B) * C

Infix:
(A + B) * C

Prefix:
* + A B C

Postfix:
A B + C *

---

## 6. Evaluate Reverse Polish Notation (RPN)

### Problem Statement

You are given an array of strings called tokens that represents an arithmetic expression in Reverse Polish Notation.

Evaluate the expression and return an integer representing its value.

### Valid Operators

- +
- -
- *
- /

### Important Conditions

1. Each operand can be an integer or another expression.
2. Division between two integers truncates toward zero.
3. There is no division by zero.
4. The input represents a valid arithmetic expression in RPN.

### Approach: Stack

A stack is used to evaluate a postfix expression.

We process the tokens from left to right.

### Algorithm

1. Create an empty stack.
2. Traverse each token in the given expression.
3. If the token is a number:
   - Convert it into an integer.
   - Push it onto the stack.
4. If the token is an operator:
   - Pop the top element from the stack and store it in b.
   - Pop the next element and store it in a.
   - Perform the operation a operator b.
   - Push the result back onto the stack.
5. After processing all tokens, the top element of the stack is the final answer.

### Important Note

The order of operands matters for subtraction and division.

For example:

Expression: ["10", "3", "-"]

First, pop 3 and store it in b.
Then, pop 10 and store it in a.

Calculate:

10 - 3 = 7

Push 7 onto the stack.

Do not calculate 3 - 10.

---

## 7. Example 1: Evaluate RPN

Input:

tokens = ["2", "1", "+", "3", "*"]

### Step-by-Step Execution

| Token | Operation | Stack |
|-------|-----------|-------|
| 2 | Push 2 | [2] |
| 1 | Push 1 | [2, 1] |
| + | 2 + 1 = 3 | [3] |
| 3 | Push 3 | [3, 3] |
| * | 3 * 3 = 9 | [9] |

Output:

9

Explanation:

First, 2 + 1 = 3.

Then, 3 * 3 = 9.

Final Answer: 9

---

## 8. Example 2: Evaluate RPN

Input:

tokens = ["8", "4", "3", "*", "+", "6", "2", "/", "-"]

### Step-by-Step Execution

| Token | Operation | Stack |
|-------|-----------|-------|
| 8 | Push 8 | [8] |
| 4 | Push 4 | [8, 4] |
| 3 | Push 3 | [8, 4, 3] |
| * | 4 * 3 = 12 | [8, 12] |
| + | 8 + 12 = 20 | [20] |
| 6 | Push 6 | [20, 6] |
| 2 | Push 2 | [20, 6, 2] |
| / | 6 / 2 = 3 | [20, 3] |
| - | 20 - 3 = 17 | [17] |

Output:

17

Explanation:

First, 4 * 3 = 12.

Then, 8 + 12 = 20.

Next, 6 / 2 = 3.

Finally, 20 - 3 = 17.

Final Answer: 17

---

## 9. Python Code

The Python program is available in:

Evaluate_Reverse_Polish_Notation.py

It uses a stack to evaluate the given postfix expression.

---

## 10. Time and Space Complexity

Let n be the number of tokens.

Time Complexity: O(n)

Each token is processed exactly once.

Space Complexity: O(n)

In the worst case, the stack can store up to n operands.

---

## 11. Key Points to Remember

1. Infix: Operator is between operands.
2. Prefix: Operator is before operands.
3. Postfix: Operator is after operands.
4. Reverse Polish Notation is another name for postfix notation.
5. A stack is used to evaluate postfix expressions.
6. Postfix expressions are evaluated from left to right.
7. Prefix expressions are typically evaluated from right to left.
8. For subtraction and division, operand order is important.
9. In RPN evaluation, the first popped operand is b, and the second popped operand is a.
10. The final result is the remaining element in the stack.