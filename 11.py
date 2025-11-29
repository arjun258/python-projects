stack = []
top = -1   # -1 means stack is empty

while True:
    print("\n1. Push")
    print("2. Pop")
    print("3. Show Stack")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item to push: ")
        stack.append(item)
        top += 1
        print(f"Pushed: {item}, top = {top}")
        print("Stack:", stack)

    elif choice == "2":
        if top == -1:
            print("Stack is empty")
        else:
            print(f"Popped: {stack.pop()}, old top = {top}")
            top -= 1
            print("Stack:", stack)

    elif choice == "3":
        print("Stack:", stack)
        print("Current top index:", top)

    elif choice == "4":
        break

    else:
        print("Invalid choice")
