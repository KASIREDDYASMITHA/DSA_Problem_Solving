# Day 31 - Implement Stack using Queues
# Stack follows LIFO - Last In First Out
# We use two queues: q1 and q2
#
# Queue operations used:
# append() -> enqueue
# pop(0)  -> dequeue from front
#
# Stack operations:
# push
# pop
# top
# size
# isEmpty

q1 = []
q2 = []

print("STACK USING TWO QUEUES")
print("----------------------")

while True:

    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Top")
    print("4. Size")
    print("5. IsEmpty")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # 1. PUSH
    if choice == 1:

        x = int(input("Enter element to push: "))

        # Step 1:
        # Insert the new element into q2.
        q2.append(x)

        # Step 2:
        # Move all elements from q1 to q2.
        #
        # This puts the newly inserted element
        # at the front of q2.
        while len(q1) > 0:

            q2.append(q1.pop(0))

        # Step 3:
        # Swap q1 and q2.
        #
        # q1 becomes the main queue.
        # q2 becomes empty.
        temp = q1
        q1 = q2
        q2 = temp

        print(x, "pushed into the stack.")

    # 2. POP
    elif choice == 2:

        # If q1 is empty, stack is empty.
        if len(q1) == 0:

            print("Stack is empty.")
            print("pop() -> -1")

        else:

            # Since the newest element is always
            # at the front of q1, dequeue it.
            removed = q1.pop(0)

            print("Popped element:", removed)

    # 3. TOP
    elif choice == 3:

        # If q1 is empty, there is no top element.
        if len(q1) == 0:

            print("Stack is empty.")
            print("top() -> -1")

        else:

            # The newest element is kept at
            # the front of q1.
            print("Top element:", q1[0])

    # 4. SIZE
    elif choice == 4:

        print("Stack size:", len(q1))

    # 5. ISEMPTY
    elif choice == 5:

        if len(q1) == 0:

            print("isEmpty() -> True")

        else:

            print("isEmpty() -> False")

    # 6. DISPLAY
    elif choice == 6:

        if len(q1) == 0:

            print("Stack is empty.")

        else:

            # q1 stores the top element at index 0.
            print("Stack from top to bottom:", q1)

    # 7. EXIT
    elif choice == 7:

        print("Program ended.")
        break

    else:

        print("Invalid choice. Please try again.")