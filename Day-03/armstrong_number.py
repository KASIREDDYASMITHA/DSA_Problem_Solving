# Day 3 - Armstrong Number

# An Armstrong number is a number in which
# the sum of each digit raised to the power
# of the total number of digits is equal to the number.
#
# Example:
# 153
#
# Number of digits = 3
#
# 1^3 + 5^3 + 3^3
# = 1 + 125 + 27
# = 153
#
# Therefore, 153 is an Armstrong Number.


n = int(input("Enter a number: "))

temp = n
count = 0
res = 0

# Count the number of digits
while n > 0:
    n = n // 10
    count += 1

n = temp

# Calculate the Armstrong sum
while n > 0:
    digit = n % 10
    res += digit ** count
    n = n // 10

if temp == res:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")