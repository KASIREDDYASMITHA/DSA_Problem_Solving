# Day 31 - Implement Queue using Stacks
# Queue follows FIFO - First In First Out
# We use two stacks: s1 and s2
#
# Stack operations used:
# append() -> push
# pop()    -> pop
#
# Queue operations:
# enqueue
# dequeue
# front
# size
# isEmpty

s1 = []
s2 = []

print("QUEUE USING TWO STACKS")
print("----------------------")

while True:

    print("\nChoose an operation:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Size")
    print("5. IsEmpty")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    # 1. ENQUEUE
    if choice == 1:

        x = int(input("Enter element to enqueue: "))

        # Enqueue means inserting into the queue.
        # We push the new element into stack s1.
        s1.append(x)

        print(x, "inserted into the queue.")

    # 2. DEQUEUE
    elif choice == 2:

        # If both stacks are empty,
        # the queue is empty.
        if len(s1) == 0 and len(s2) == 0:

            print("Queue is empty.")
            print("dequeue() -> -1")

        else:

            # If s2 is empty, transfer all elements
            # from s1 to s2.
            #
            # This reverses the order and makes
            # the oldest element available on top of s2.
            if len(s2) == 0:

                while len(s1) > 0:

                    s2.append(s1.pop())

            # The front element is now at the top of s2.
            removed = s2.pop()

            print("Dequeued element:", removed)

    # 3. FRONT
    elif choice == 3:

        # If both stacks are empty,
        # there is no front element.
        if len(s1) == 0 and len(s2) == 0:

            print("Queue is empty.")
            print("front() -> -1")

        else:

            # If s2 is empty, move all elements
            # from s1 to s2.
            if len(s2) == 0:

                while len(s1) > 0:

                    s2.append(s1.pop())

            # The top element of s2 is the front.
            print("Front element:", s2[-1])

    # 4. SIZE
    elif choice == 4:

        # Total number of elements is the
        # number of elements in both stacks.
        total = len(s1) + len(s2)

        print("Queue size:", total)

    # 5. ISEMPTY
    elif choice == 5:

        # Queue is empty only when both stacks are empty.
        if len(s1) + len(s2) == 0:

            print("isEmpty() -> True")

        else:

            print("isEmpty() -> False")

    # 6. DISPLAY
    elif choice == 6:

        if len(s1) == 0 and len(s2) == 0:

            print("Queue is empty.")

        else:

            # Create a temporary list only for displaying
            # the queue from front to rear.
            temp = []

            # Elements already present in s2 are in
            # front-to-rear order when read from top to bottom.
            for i in range(len(s2) - 1, -1, -1):

                temp.append(s2[i])

            # Elements in s1 are stored in reverse order,
            # so read them from bottom to top.
            for i in range(len(s1)):

                temp.append(s1[i])

            print("Queue from front to rear:", temp)

    # 7. EXIT
    elif choice == 7:

        print("Program ended.")
        break

    else:

        print("Invalid choice. Please try again.")