"""
Student Grade Manager
Week 1 - Day 2 assignment

Run with:
    python grade_manager.py
"""

# A list stores one dictionary per student.
# This allows duplicate names because each student is a separate record.
students = []


def get_grade(mark):
    """Return the grade for a mark between 0 and 100."""
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "E"


def add_student():
    """Ask for a student's name and mark, validate them, and save the record."""
    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty. Student was not added.")
        return

    mark_input = input("Enter mark (0-100): ").strip()

    try:
        mark = float(mark_input)
    except ValueError:
        print("Invalid mark. Please enter a number, such as 85 or 92.5.")
        return

    if not 0 <= mark <= 100:
        print("Mark must be between 0 and 100. Student was not added.")
        return

    students.append({
        "name": name,
        "mark": mark,
        "grade": get_grade(mark)
    })

    print(f"{name} was added successfully.")


def show_results():
    """Display the student table and class statistics."""
    if not students:
        print("\nNo student records yet. Add a student first.")
        return

    print("\n" + "=" * 42)
    print(f"{'Name':<20}{'Mark':>10}{'Grade':>10}")
    print("-" * 42)

    for student in students:
        print(
            f"{student['name']:<20}"
            f"{student['mark']:>10.1f}"
            f"{student['grade']:>10}"
        )

    marks = [student["mark"] for student in students]
    average = sum(marks) / len(marks)

    print("-" * 42)
    print(f"Average: {average:.1f}")
    print(f"Highest: {max(marks):.1f}")
    print(f"Lowest:  {min(marks):.1f}")
    print("=" * 42)


def main():
    """Keep showing the menu until the user chooses to quit."""
    while True:
        print("\n===== Student Grade Manager =====")
        print("1. Add student")
        print("2. Show results")
        print("3. Quit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_results()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid menu option. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
