# Day 31 - Stack & Queue - 6

## 📚 Topics Covered

Today I learned how to implement one data structure using another data structure.

### 1. Queue using Stacks
- Implement Queue using two Stacks
- Queue follows FIFO (First In First Out)
- Operations:
  - enqueue()
  - dequeue()
  - front()
  - size()
  - isEmpty()

### 2. Stack using Queues
- Implement Stack using two Queues
- Stack follows LIFO (Last In First Out)
- Operations:
  - push()
  - pop()
  - top()
  - size()
  - isEmpty()

## 🧠 Key Concepts

### Queue using Stacks

Two stacks are used:

- Stack 1 → used for inserting elements
- Stack 2 → used for removing elements

When Stack 2 is empty, elements are transferred from Stack 1 to Stack 2.

This reversal makes the oldest element available at the top of Stack 2.

### Stack using Queues

Two queues are used.

During `push()`:
1. Insert the new element into the second queue.
2. Move all elements from the first queue to the second queue.
3. Swap the two queues.

This keeps the newest element at the front of the main queue.

## ⏱️ Complexity

### Queue using Stacks

- `enqueue()` → O(1)
- `dequeue()` → O(n) worst case
- `front()` → O(n) worst case
- `size()` → O(1)
- `isEmpty()` → O(1)

### Stack using Queues

- `push()` → O(n)
- `pop()` → O(1)
- `top()` → O(1)
- `size()` → O(1)
- `isEmpty()` → O(1)


