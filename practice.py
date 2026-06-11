# 1. Initialize the list with default names
students = ["Ram", "Hari"]

# Set a maximum number of operations the user can perform (e.g., 100)
max_operations = 100

for i in range(max_operations):
    # 2. Display the menu-driven interface
    print("\n--- Student Management System ---")
    print("1. Create (Add Student)")
    print("2. Read (View Students)")
    print("3. Update (Edit Student)")
    print("4. Delete (Remove Student)")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    # Choice 1: Create
    if choice == "1":
        name = input("Enter the student's name: ").strip()
        if name:
            students.append(name)
            print(f"Success: '{name}' has been added.")
        else:
            print("Error: Name cannot be empty.")

    # Choice 2: Read
    elif choice == "2":
        # 3. Handle empty lists gracefully
        if not students:
            print("Notification: The student list is currently empty.")
        else:
            print("\n--- Current Student List ---")
            for index, name in enumerate(students):
                print(f"Index {index}: {name}")

    # Choice 3: Update
    elif choice == "3":
        if not students:
            print("Error: No students available to update.")
            continue  # Skips to the next iteration of the for loop

        try:
            index = int(input("Enter the index number to update: "))
            # Verification to prevent errors
            if 0 <= index < len(students):
                new_name = input("Enter the new name: ").strip()
                if new_name:
                    old_name = students[index]
                    students[index] = new_name
                    print(
                        f"Update Complete: '{old_name}' changed to '{new_name}'."
                    )
                else:
                    print("Error: New name cannot be empty.")
            else:
                print("Error: Index out of range. Please view the list first.")
        except ValueError:
            print("Error: Please enter a valid numerical index.")

    # Choice 4: Delete
    elif choice == "4":
        if not students:
            print("Error: No students available to delete.")
            continue  # Skips to the next iteration of the for loop

        try:
            index = int(input("Enter the index number to delete: "))
            # Verification to prevent errors
            if 0 <= index < len(students):
                removed_student = students.pop(index)
                print(f"Delete Complete: Removed '{removed_student}'.")
            else:
                print("Error: Index out of range. Please view the list first.")
        except ValueError:
            print("Error: Please enter a valid numerical index.")

    # Choice 5: Exit
    elif choice == "5":
        print("Program terminated. Goodbye!")
        break  # Breaks out of the for loop entirely

    else:
        print("Invalid Choice: Please select a valid option from 1 to 5.")