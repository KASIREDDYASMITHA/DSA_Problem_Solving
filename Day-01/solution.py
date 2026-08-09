# DSA Day 1 - Flowcharts and Conditional Statements

# ============================================================
# Question 1: Calculate the area of a rectangle.
# Input: Length and breadth
# Output: Area of the rectangle
# ============================================================

length = int(input("Enter the length: "))
breadth = int(input("Enter the breadth: "))

area = length * breadth

print("Area:", area)


# ============================================================
# Question 2: Given an integer N, determine whether the number
# is even or odd.
# Input: An integer N
# Output: "Even" if N is divisible by 2, otherwise "Odd"
# ============================================================

n = int(input("Enter N value: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# ============================================================
# Question 3: Given an integer N, determine whether the number
# is positive, negative, or zero.
# Input: An integer N
# Output: "P" for positive, "N" for negative, and "Z" for zero
# ============================================================

n = int(input("Enter N value: "))

if n > 0:
    print("P")
elif n < 0:
    print("N")
else:
    print("Z")


# ============================================================
# Question 4: Given three numbers A, B and C, find the largest
# number.
# Input: Three integers A, B and C
# Output: The largest of the three numbers
# ============================================================

a = int(input("Enter A value: "))
b = int(input("Enter B value: "))
c = int(input("Enter C value: "))

if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)


# ============================================================
# Question 5: Given a year, determine whether it is a leap year
# or not.
# Input: A year
# Output: "Leap Year" if it is a leap year, otherwise
# "Not a Leap Year"
# ============================================================

year = int(input("Enter year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not a Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")


# ============================================================
# Question 6: Given marks, print the corresponding grade.
# Input: Marks
# Output:
# 90 or above -> A
# 75 to 89    -> B
# 60 to 74    -> C
# 40 to 59    -> D
# Below 40    -> F
# ============================================================

marks = int(input("Enter marks: "))

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("F")


# ============================================================
# Question 7: Given an integer N, follow the Fizz Buzz conditions.
# Input: An integer N
# Output:
# If N is divisible by 15, print "FB"
# Else if N is divisible by 3, print "FZ"
# Else if N is divisible by 5, print "BZ"
# Otherwise calculate X = N * 2, S = N + X and print S
# ============================================================

n = int(input("Enter N value: "))

if n % 15 == 0:
    print("FB")
elif n % 3 == 0:
    print("FZ")
elif n % 5 == 0:
    print("BZ")
else:
    x = n * 2
    s = n + x
    print(s)