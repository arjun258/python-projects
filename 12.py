queue = []
front = -1
rear = -1

while True:
    print("\n1. Insert (Enqueue)")
    print("2. Delete (Dequeue)")
    print("3. Show Queue")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item to insert: ")
        queue.append(item)

        if front == -1:      # first element
            front = 0

        rear += 1
        print(f"Inserted: {item}, front = {front}, rear = {rear}")
        print("Queue:", queue)

    elif choice == "2":
        if front == -1:      # queue empty
            print("Queue is empty")
        else:
            print(f"Deleted: {queue[0]}, front = {front}")
            queue.pop(0)     # actually remove from front

            if not queue:    # queue became empty
                front = -1
                rear = -1
            else:
                rear -= 1    # size reduced by 1

            print("Queue:", queue)

    elif choice == "3":
        print("Queue:", queue)
        print(f"front = {front}, rear = {rear}")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
