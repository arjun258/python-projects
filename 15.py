import pickle
import os

def add_record():
    record = {}
    record["rollno"] = int(input("Roll number: "))
    record["name"] = input("Name: ")
    record["marks"] = int(input("Marks: "))

    mode = "ab" if os.path.exists("student.dat") else "wb+"

    with open("student.dat", mode) as f:
        pickle.dump(record, f)

    print("Record added.")

def show_high_scorers():
    print("\nStudents with marks > 80:")
    try:
        with open("student.dat", "rb") as f:
            while True:
                rec = pickle.load(f)
                if rec["marks"] > 80:
                    print(rec)
    except FileNotFoundError:
        print("No records found yet.")
    except EOFError:
        pass

while True:
    print("\n1. Add record")
    print("2. Show records with marks > 80")
    print("3. Exit")

    choice = input("Choice: ")

    if choice == "1":
        add_record()
    elif choice == "2":
        show_high_scorers()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
