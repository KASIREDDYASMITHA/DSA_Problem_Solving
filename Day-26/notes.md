# DSA Day 26 Notes

# Stack and Queue

## 1. Abstract Data Type (ADT)

An Abstract Data Type describes a data structure based on the operations that can be performed on it.

ADT focuses on:

* What operations are supported.
* What those operations do.
* Not how they are implemented internally.

A Stack is an ADT.

It can be implemented using:

* Arrays
* Linked Lists
* Other data structures

The implementation can change, but the behavior of the Stack remains the same.

---

# 2. Stack

A Stack is a linear data structure that follows:

## LIFO

**Last In First Out**

The element inserted last is removed first.

### Example

Suppose we insert:

```text
10
20
30
```

The top element is:

```text
30
```

If we perform `pop()`, 30 is removed first.

Then:

```text
20
```

becomes the top element.

---

# 3. Stack Operations

## Push

`push` is used to insert an element into the Stack.

The new element is added at the top.

Example:

```text
push(10)
push(20)
push(30)
```

Stack:

```text
30 ← Top
20
10
```

---

## Pop

`pop` removes the element from the top of the Stack.

Example:

```text
Stack:

30 ← Top
20
10
```

After:

```text
pop()
```

30 is removed.

Stack becomes:

```text
20 ← Top
10
```

---

## Peek

`peek` returns the top element without removing it.

Example:

```text
Stack:

30 ← Top
20
10
```

`peek()` returns:

```text
30
```

The Stack remains unchanged.

---

## isEmpty

Checks whether the Stack contains no elements.

For an array implementation:

```text
top == -1
```

means the Stack is empty.

---

## isFull

Checks whether the Stack has reached its maximum capacity.

For an array implementation:

```text
top == MAX_SIZE - 1
```

means the Stack is full.

---

# 4. Stack Using Array

A Stack can be implemented using an array.

For a fixed-size array:

```text
stack = [0] * MAX_SIZE
```

Initially:

```text
top = -1
```

## Push

Steps:

1. Check whether the Stack is full.
2. Increase `top`.
3. Store the element at `stack[top]`.

## Pop

Steps:

1. Check whether the Stack is empty.
2. Take the element from `stack[top]`.
3. Decrease `top`.

## Peek

Steps:

1. Check whether the Stack is empty.
2. Return `stack[top]`.

---

# 5. Stack Example

```text
push(10)
push(20)
push(30)
pop()
```

Output:

```text
30
```

Because Stack follows LIFO.

Another example:

```text
push(10)
push(20)
push(30)
push(40)
peek()
```

Output:

```text
40
```

---

# 6. Queue

A Queue is a linear data structure that follows:

## FIFO

**First In First Out**

The element inserted first is removed first.

### Example

Suppose we insert:

```text
10
20
30
```

The first element is:

```text
10
```

If we perform `dequeue()`, 10 is removed first.

---

# 7. Queue Operations

## Enqueue

`enqueue` is used to insert an element into the Queue.

The element is added at the rear.

Example:

```text
enqueue(10)
enqueue(20)
enqueue(30)
```

Queue:

```text
Front → 10  20  30 ← Rear
```

---

## Dequeue

`dequeue` removes an element from the front of the Queue.

Example:

```text
Front → 10  20  30 ← Rear
```

After:

```text
dequeue()
```

10 is removed.

Queue becomes:

```text
Front → 20  30 ← Rear
```

---

## Peek

`peek` returns the front element without removing it.

Example:

```text
Front → 20  30 ← Rear
```

`peek()` returns:

```text
20
```

The Queue remains unchanged.

---

# 8. Queue Example

The faculty notes use this sequence:

```text
enqueue(10)
enqueue(20)
enqueue(30)
dequeue()
enqueue(40)
dequeue()
enqueue(50)
peek()
```

Queue follows FIFO, so the first inserted elements are removed first.

---

# 9. Stack vs Queue

| Stack             | Queue               |
| ----------------- | ------------------- |
| LIFO              | FIFO                |
| Last In First Out | First In First Out  |
| Insertion at Top  | Insertion at Rear   |
| Deletion from Top | Deletion from Front |
| push              | enqueue             |
| pop               | dequeue             |
| peek              | peek                |

## Remember

```text
STACK  → LIFO
QUEUE  → FIFO
```
