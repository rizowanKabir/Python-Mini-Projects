"""
Student Grade Management System

Features:
1. Add Student
2. Update Student
3. Delete Student
4. View All Students
5. Exit
"""

# Dictionary to store student grades
student_grades = {}


# Add Student
def add_student(name, grade):
    if name in student_grades:
        print(f"\n{name} already exists!")
    else:
        student_grades[name] = grade
        print(f"\n{name} added successfully with grade {grade}.")


# Update Student
def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"\n{name}'s grade updated to {grade}.")
    else:
        print(f"\n{name} not found!")


# Delete Student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"\n{name} deleted successfully.")
    else:
        print(f"\n{name} not found!")


# View All Students
def view_students():
    if student_grades:
        print("\n===== Student List =====")
        for name, grade in student_grades.items():
            print(f"Name : {name} | Grade : {grade}")
    else:
        print("\nNo students found.")


# Main Function
def main():
    while True:
        print("\n========== Student Grade Management System ==========")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View All Students")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            name = input("Enter student name: ")

            try:
                grade = float(input("Enter student grade: "))
                add_student(name, grade)
            except ValueError:
                print("Invalid grade! Please enter a number.")

        elif choice == "2":
            name = input("Enter student name: ")

            try:
                grade = float(input("Enter new grade: "))
                update_student(name, grade)
            except ValueError:
                print("Invalid grade! Please enter a number.")

        elif choice == "3":
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == "4":
            view_students()

        elif choice == "5":
            print("\nThank you for using the Student Grade Management System.")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 5.")

# Run the program
if __name__ == "__main__":
    main()