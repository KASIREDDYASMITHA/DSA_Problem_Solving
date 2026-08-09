# Alternative approaches practiced on Day 1


# 1. Even or Odd using Bitwise AND

n = int(input("Enter N value: "))

if n & 1:
    print("Odd")
else:
    print("Even")


# 2. Leap Year using a Combined Condition

year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")