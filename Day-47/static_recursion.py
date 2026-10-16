# Persistent counter for fun1().
fun1_i = 0

# Persistent counter for fun2().
fun2_i = 0


def fun1(n):
    global fun1_i

    if n > 0:
        # Increment the persistent counter.
        fun1_i = fun1_i + 1

        # Recursive call.
        fun1(n - 1)

    # Return the current persistent value.
    return fun1_i


def fun2(n):
    global fun2_i

    if n > 0:
        # Add the return value of fun1(n).
        fun2_i = fun2_i + fun1(n)

        # Recursive call.
        fun2(n - 1)

    # Return the current persistent value.
    return fun2_i


# Execute the faculty example.
result = fun2(5)

print("Return value of fun2(5):", result)
