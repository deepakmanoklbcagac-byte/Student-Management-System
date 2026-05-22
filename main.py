import mysql.connector

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="deepak123",
    database="studentdb"
)

cursor = db.cursor()

# Add Student
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    phone = input("Enter Phone: ")

    sql = "INSERT INTO students (name, age, course, phone) VALUES (%s, %s, %s, %s)"
    values = (name, age, course, phone)

    cursor.execute(sql, values)
    db.commit()

    print("Student Added Successfully!")

# View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    print("\nStudent Records")
    print("-" * 50)

    for row in result:
        print(row)

# Update Student
def update_student():
    student_id = int(input("Enter Student ID: "))
    new_phone = input("Enter New Phone Number: ")

    sql = "UPDATE students SET phone=%s WHERE id=%s"
    values = (new_phone, student_id)

    cursor.execute(sql, values)
    db.commit()

    print("Student Updated Successfully!")

# Delete Student
def delete_student():
    student_id = int(input("Enter Student ID: "))

    sql = "DELETE FROM students WHERE id=%s"
    values = (student_id,)

    cursor.execute(sql, values)
    db.commit()

    print("Student Deleted Successfully!")

# Main Menu
while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == '1':
        add_student()

    elif choice == '2':
        view_students()

    elif choice == '3':
        update_student()

    elif choice == '4':
        delete_student()

    elif choice == '5':
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")