# DSA Learning - Day 37

## Topic: Binary Search on Answer

Today I learned the concept of **Binary Search on Answer** and practiced it using two problems.

### Problems Covered

1. Koko Eating Bananas
2. Minimum Number of Days to Make m Bouquets

---

## 1. Koko Eating Bananas

### Problem

Koko has several piles of bananas. She has `h` hours to eat all the bananas.

If Koko eats at speed `k` bananas per hour, she takes:

`ceil(pile / k)` hours to finish each pile.

The goal is to find the **minimum eating speed** that allows Koko to finish all the bananas within `h` hours.

### Approaches

- Brute Force
- Binary Search

### Brute Force

Try every possible eating speed from `1` to `max(piles)`.

For every speed, calculate the total hours required.

The first speed that finishes all bananas within `h` hours is the answer.

### Binary Search

The possible answer lies between:

- Low = `1`
- High = `max(piles)`

For every middle speed:

- If Koko can finish within `h` hours, search for a smaller speed.
- Otherwise, search for a larger speed.

---

## 2. Minimum Number of Days to Make m Bouquets

### Problem

We are given an array where each value represents the day a flower blooms.

A bouquet requires `k` **adjacent flowers**.

We need to make at least `m` bouquets.

The goal is to find the **minimum number of days** required to make `m` bouquets.

### Important Condition

If:

`m * k > len(bloomDay)`

then it is impossible to make the required number of bouquets.

Return `-1`.

### Approaches

- Brute Force
- Binary Search

### Brute Force

Try every possible day from the minimum bloom day to the maximum bloom day.

For each day:

- Count flowers that have bloomed.
- Count consecutive flowers.
- Form bouquets using groups of `k` adjacent flowers.
- Check whether at least `m` bouquets can be formed.

### Binary Search

The possible answer lies between:

- Low = minimum bloom day
- High = maximum bloom day

For every middle day:

- Count the bouquets possible by that day.
- If enough bouquets can be made, search for an earlier day.
- Otherwise, search for a later day.

---

## Key Learning

Binary Search on Answer is useful when:

- The answer lies in a sorted range.
- We can check whether a particular answer is possible.
- If one value is possible, all larger or smaller values follow a predictable pattern.

The main idea is:

**Search for the minimum possible valid answer.**