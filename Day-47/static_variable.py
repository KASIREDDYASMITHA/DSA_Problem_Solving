# Initialize the persistent variable only once.
static_x = 1


def funcp():
    global static_x

    # Increment the persistent variable.
    static_x = static_x + 1

    # Return its updated value.
    return static_x


# First function call.
x = funcp()

# Second function call.
y = funcp() + x

# Display the result.
print("x =", x)
print("y =", y)
print("x + y =", x + y)
