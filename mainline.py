import sqlite3

def display_students(cur):

    print("\nStudent Records")
    print("-" * 90)

    cur.execute("SELECT * FROM students")
    records = cur.fetchall()

    print(f"{'ID':<6}{'First Name':<15}{'Last Name':<15}"
          f"{'Age':<6}{'Major':<20}{'GPA':<6}{'Grad Year':<10}")
    print("-" * 90)

    for record in records:
        print(f"{record[0]:<6}{record[1]:<15}{record[2]:<15}"
              f"{record[3]:<6}{record[4]:<20}{record[5]:<6}"
              f"{record[7]:<10}")


def edit_student(conn, cur):
    """Edit a student record"""

    student_id = int(input("\nEnter Student ID to edit: "))

    cur.execute("SELECT * FROM students WHERE student_id = ?", (student_id,))
    student = cur.fetchone()

    if student is None:
        print("Student not found.")
        return

    print("\nCurrent Student Information:")
    print(student)

    print("\nWhat would you like to edit?")
    print("1. First Name")
    print("2. Last Name")
    print("3. Age")
    print("4. Major")
    print("5. GPA")
    print("6. Email")
    print("7. Graduation Year")

    choice = input("Enter choice (1-7): ")

    fields = {
        "1": "first_name",
        "2": "last_name",
        "3": "age",
        "4": "major",
        "5": "gpa",
        "6": "email",
        "7": "grad_year"
    }

    if choice not in fields:
        print("Invalid choice.")
        return

    new_value = input("Enter new value: ")

    if choice == "3" or choice == "7":
        new_value = int(new_value)
    elif choice == "5":
        new_value = float(new_value)

    sql = f"UPDATE students SET {fields[choice]} = ? WHERE student_id = ?"

    cur.execute(sql, (new_value, student_id))
    conn.commit()

    print("Record updated successfully.")


def main():

    conn = sqlite3.connect('students.db')
    cur = conn.cursor()

    while True:

        print("\n===== STUDENT DATABASE MENU =====")
        print("1. Display All Students")
        print("2. Edit Student Record")
        print("3. Exit")

        option = input("Enter your choice: ")

        if option == "1":
            display_students(cur)

        elif option == "2":
            display_students(cur)
            edit_student(conn, cur)

        elif option == "3":
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")

    conn.close()

main()
