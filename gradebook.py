# Student Gradebook Manager - Mosa Ndlovu - Python Essentials 1

# Returns the average of a list of marks, or None if the list is empty
def calculate_average(marks):
    ...

# Returns the highest and lowest mark as a tuple: (highest, lowest)
def highest_and_lowest(marks):
    ...

# Asks for a mark, validates it with try-except,returns the float or None
def read_valid_mark():
    ...

# Adds a new student to the gradebook dictionary
def add_student(gradebook):
    name = input("Student name: ").strip()

    if name == "":
        print("back to menu.")
        return

    if name in gradebook:
        print(name + " already exists.")
        return

    gradebook[name] = []
    print(name + " added.")   

# Adds one validated mark to an existing student
def add_mark(gradebook):
    ...

# Prints every student with marks and average
def view_all(gradebook):
    ...

# Prints one student's full summary
def student_summary(gradebook):
    ...

# Prints class statistics including pass/fail lists
def class_statistics(gradebook):
    ...

# Removes a student after y/n confirmation
def remove_student(gradebook):
    ...

# ---- main program ----
gradebook = {}

while True:
    # print the menu ,read the choice,call the right function
    print("\n===== STUDENT GRADEBOOK MANAGER =====")
    print("1. Add a student")
    print("2. Add a mark")
    print("3. View all students")
    print("4. Student summary")
    print("5. Class statistics")
    print("6. Remove a student")
    print("7. Exit")

    choice = input("Choose an option (1-7): ")

    if choice == "1":
        add_student(gradebook)

    elif choice == "2":
        print("Add mark feature coming soon.")

    elif choice == "3":
        print("View all feature coming soon.")

    elif choice == "4":
        print("Student summary feature coming soon.")

    elif choice == "5":
        print("Class statistics feature coming soon.")

    elif choice == "6":
        print("Remove student feature coming soon.")

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please enter 1-7.")
