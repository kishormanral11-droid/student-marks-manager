marks = {
    "Rahul": 85,
    "Aman": 92,
    "Riya": 92,
    "Karan": 78,
    "Neha": 88
}
passing_marks = 33
def get_valid_choice():
    while True:
        try:
            choice = int(input("Enter a choice from (1-6): "))
            if 1 <=choice <= 6:
                return choice
            else:
                print("Please enter number between 1-6!!!")
            
        except ValueError:
            print("Please enter a number according to your choice!!!!!")
def get_valid_name():
    while True:
        name = input("Enter a student's name: ")
        name = name.title()
        if name == "":
            print("Please enter a valid name!!!!")
        elif name.isdigit():
            print("Please enter a valid name.")
        else:
            if name in marks:
                print("Name already exists in marks!!!")
            else:
                return name
def get_valid_marks():
    while True:
        try:
            student_marks = int(input("Please enter marks in numbers: "))
            if 0 <= student_marks <= 100:
                print("Marks added successfully!!!")
                return student_marks
            else:
                print("Please enter marks from 0 to 100!!")
            
        except ValueError:
            print("Please enter valid number!!!!")
def get_existing_name():
    while True:
        name = input("Enter a student's name: ")
        name = name.title()
        if name == "":
            print("Please enter a valid name!!!!")
        else:
            if name in marks:
                return name
            else:
                print("Please enter a name that already exit for update!!!")
                print("Students name not found!!!!")
def get_student_status(student_marks):
    if student_marks >= passing_marks:
        return "Pass!!!"
    else:
        return "Fail, Try again!!!"
def show_students():
    print("------ Student List ------")
    for name in marks:
        print(name, ":", marks[name])
def add_students():
    student_name = get_valid_name()
    student_marks = get_valid_marks()
    marks[student_name] = student_marks
    print("Student added successfully...")
    show_students()
def update_marks():
    student = get_existing_name()
    print("-----Student found-----")
    student_marks = get_valid_marks()
    marks[student] = student_marks
    print("Marks updated successfully.")
    show_students()
def delete_student():
    student = get_existing_name()
    del marks[student]
    print("Student deleted successfully.")
    show_students()
def search_student():
    search_stu = get_existing_name()
    student_marks = marks[search_stu]
    status = get_student_status(student_marks)
    print("=====Students Details=====")
    print("Name: ", search_stu)
    print("Marks: ", student_marks)
    print("Status: ", status )

while True:
    print("""
         ===== Student Marks Manager =====
        1. Show Students
        2. Add Student
        3. Update Marks
        4. Delete Student
        5. Search Student
        6. Exit""")
    choice = get_valid_choice()

    if choice == 1:
        show_students()
    elif choice == 2:
        add_students()
    elif choice == 3:
        update_marks()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        search_student()
    elif choice == 6:
        print("Thank you for using Student marks manager!!☺️ ")
        break