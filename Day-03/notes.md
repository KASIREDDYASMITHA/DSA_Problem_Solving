# DSA Day 3 - Loops 2

## Topics Covered

1. Prime Number
2. Different approaches to check Prime Number
3. Perfect Number
4. Better approach using Square Root
5. Armstrong Number

---

# 1. Prime Number

A prime number is a number greater than 1 that has exactly two positive divisors:

- 1
- The number itself

### Examples

2 -> 1, 2 -> Prime

7 -> 1, 7 -> Prime

### Non-Prime Example

6 -> 1, 2, 3, 6

Since 6 has more than two divisors, it is not prime.

---

## Approach 1: Count the Divisors

We can check every number from 1 to n.

If n is divisible by i, then i is a divisor of n.

We count the total number of divisors.

If the count is exactly 2, the number is prime.

### Time Complexity

O(n)

### Space Complexity

O(1)

---

## Approach 2: Check Factors up to Square Root

If a number n is composite, it must have a factor less than or equal to sqrt(n).

Therefore, instead of checking from 2 to n-1, we only need to check:

2 to sqrt(n)

### Example

For n = 36:

sqrt(36) = 6

We only need to check factors from 2 to 6.

36 % 2 == 0

Therefore, 36 is not prime.

### Time Complexity

O(sqrt(n))

### Space Complexity

O(1)

---

# 2. Perfect Number

A perfect number is a number whose positive divisors, excluding the number itself, have a sum equal to the number.

### Example

6

Divisors excluding 6:

1, 2, 3

1 + 2 + 3 = 6

Therefore, 6 is a Perfect Number.

### Another Example

28

Divisors excluding 28:

1, 2, 4, 7, 14

1 + 2 + 4 + 7 + 14 = 28

Therefore, 28 is a Perfect Number.

### Non-Perfect Example

36

Divisors excluding 36:

1, 2, 3, 4, 6, 9, 12, 18

Sum:

1 + 2 + 3 + 4 + 6 + 9 + 12 + 18 = 55

Since 55 != 36, 36 is not a Perfect Number.

---

## Perfect Number - Brute Force Approach

Check all numbers from 1 to n-1.

If n is divisible by i, add i to the sum.

Finally:

sum == n -> Perfect Number

sum != n -> Not a Perfect Number

### Time Complexity

O(n)

### Space Complexity

O(1)

---

## Perfect Number - Better Approach

We can use the fact that divisors occur in pairs.

For example:

36

2 x 18 = 36

3 x 12 = 36

4 x 9 = 36

6 x 6 = 36

Therefore, when we find a divisor i, we can also find its pair:

pair = n // i

We only need to check up to sqrt(n).

### Time Complexity

O(sqrt(n))

### Space Complexity

O(1)

---

# 3. Armstrong Number

An Armstrong number is a number in which the sum of each digit raised to the power of the total number of digits is equal to the original number.

### Example

153

Number of digits = 3

1^3 + 5^3 + 3^3

= 1 + 125 + 27

= 153

Therefore, 153 is an Armstrong Number.

### Another Example

370

Number of digits = 3

3^3 + 7^3 + 0^3

= 27 + 343 + 0

= 370

Therefore, 370 is an Armstrong Number.

---

## Armstrong Number Algorithm

### Step 1

Find the number of digits.

### Step 2

Extract each digit using:

digit = n % 10

### Step 3

Raise the digit to the power of the total number of digits.

### Step 4

Add all the results.

### Step 5

Compare the result with the original number.

If:

result == original number

then it is an Armstrong Number.

Otherwise, it is not an Armstrong Number.

---

## Important Operations

### Extract last digit

digit = n % 10

### Remove last digit

n = n // 10

### Find paired divisor

pair = n // i

### Square Root

sqrt(n)

---

# Complexity Summary

| Problem | Approach | Time Complexity | Space Complexity |
|---------|----------|------------------|------------------|
| Prime | Brute Force | O(n) | O(1) |
| Prime | Square Root | O(sqrt(n)) | O(1) |
| Perfect Number | Brute Force | O(n) | O(1) |
| Perfect Number | Square Root | O(sqrt(n)) | O(1) |
| Armstrong | Digit Processing | O(d) | O(1) |

Here d represents the number of digits.