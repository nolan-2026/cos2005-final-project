# Student Database Setup Program
# Creates a database and adds sample student records

import sqlite3


def main():

    conn = sqlite3.connect('students.db')

    cur = conn.cursor()

    # Students table
    cur.execute('''
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            age INTEGER,
            major TEXT,
            gpa REAL,
            email TEXT,
            grad_year INTEGER
        )
    ''')

    # Student data
    students = [
        (101, 'John', 'Smith', 20, 'Computer Science', 3.5, 'johnsmith@email.com', 2027),
        (102, 'Sarah', 'Lee', 21, 'Nursing', 3.8, 'sarahlee@email.com', 2026),
        (103, 'Michael', 'Brown', 19, 'Business', 3.2, 'michaelbrown@email.com', 2028),
        (104, 'Emily', 'Davis', 22, 'Psychology', 3.9, 'emilydavis@email.com', 2025),
        (105, 'Daniel', 'Wilson', 20, 'Engineering', 3.4, 'danielwilson@email.com', 2027)
    ]

    # Insert records into table
    cur.executemany('''
        INSERT OR IGNORE INTO students
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', students)

    # Save changes
    conn.commit()

    # Display all records
    print("Student Records")
    print("-----------------------------")

    cur.execute("SELECT * FROM students")

    records = cur.fetchall()

    for record in records:
        print(record)

    # Close database
    conn.close()

main()
