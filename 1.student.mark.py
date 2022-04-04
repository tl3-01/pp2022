import re
import datetime
students = {}
courses = {}
# Input number of students
def studentNumber():
    global student_num
    while True:
        try:
            student_num = input('Enter the number of students in a class: ')
            student_num = int(student_num)
            if student_num <= 0:
                print("The number of students must be positive. Try again!")
                continue
        except ValueError:
            print("The number of students must be a number. Try again!")
        else:
            return student_num
    
# Input number of courses
def courseNumber():
    global course_num
    while True:
        try:
            course_num = input('Enter the number of courses: ')
            course_num = int(course_num)
            if course_num <= 0:
                print("The number of courses must be positive. Try again!")
                continue
        except ValueError:
            print("The number of courses must be a number. Try again!")
        else:
            return course_num

# Get student ID, name, dob
def studentInfo():
    global students
    for i in range(0, student_num):
        print(f"\n--- Input the data for student {i+1} ---")
        prefix = ''
        while True:
            prefix = input("Please enter one of the prefix \"BI11\" or \"BA10\" for the student ID: ")
            if prefix not in {"BI11", "BA10"}:
                print("The prefix must be \"BI11\" or \"BA10\. Try again!")
            else:
                break
        while True:
            id_number = input("Please input last 3 digits of student ID: ")
            try:
                idNumber = int(id_number);
                if idNumber <= 0:
                    print("The ID number must be positive. Try again!")
                elif len(id_number) != 3:
                    print("The ID number is 3 digits. Try again!")
                else:
                    break
            except ValueError:
                print("The ID number must be a number. Try again!")
        sId = prefix + "-" + str(id_number)
        
        while True:
            name = input("Please input student name: ")
            if not re.match(r'[a-zA-Z\s]+$', name):
                print ("Error! Make sure you only use letters in the student name.")
            else:
                break

        while True:
            DoB = input("Please input student DoB (Input format: dd/mm/yyyy): ")
            try:
                dob = datetime.datetime.strptime(DoB,"%d/%m/%Y").date()
            except ValueError:
                print("Wrong format for DoB. Try again!")
            else:
                break
        
        students[sId] = {
            "name": name,
            "DoB": DoB,
            "marks" : {}
        }
    return students

# Get course id and name
def courseInfo():
    global courses
    for i in range(0, course_num):
        while True:
            sId = input(f"\n--- Input the data for course {i+1} ---\nPlease enter the course Id: ")
            try:
                courseId = int(sId);
                if courseId < 0:
                    print("The ID number can't be negative. Try again!")
                elif len(sId) != 2:
                    print("The ID number is 2 digits. Try again!")
                elif str(courseId) == '000':
                    print("The ID number can't be all 0s. Try again!")
                else:
                    break
            except ValueError:
                print("The ID number must be a number. Try again!")
        while True:
            name = input("Please input course name: ")
            if not re.match(r'[a-zA-Z\s]+$', name):
                print ("Error! Make sure you only use letters in the course name.")
            else:
                break
        courses[sId] = {
            "name": name
        }
    return courses

# Validation if course exist or not
def validationCourse():
    if not courses:
        print("The course list empty, please add more course(s)!")
        return
    elif not students:
        print("The student list empty, please add more student(s)!")
        return
    global coursename
    for sId in courses:
        while True:
            coursename = input("\nEnter the course name: ")
            if coursename == courses[sId]['name']:
                print(f"The course {coursename} is in course list, please continue.")
                return coursename
            else:
                print(f"The course {coursename} is not in course list. Try again!")
                continue
            
                
# Select course and input the mark of students in this course
def studentMark():
    for sId in students:
        while True:
            mark = input(f"- Student {students[sId]['name']}: ")     
            try:
                mark = float(mark)
                if mark > 20.0 or mark < 0.0:
                    print("The mark must be between 0 and 20. Try again!")
                else:
                    students[sId]['marks'][coursename] = mark
                    break
            except ValueError:
                print("Wrong data type for mark. Try again!")

# Print the student list
def studentList():
    if not students:
        print("The student list empty, please add more student(s)!")
        return
    print("All students list: ")
    for sId in students:
        print(f"Student ID: {sId} \nStudent Name: {students[sId]['name']} \nStudent DoB: {students[sId]['DoB']}")

# Print the course list
def courseList():
    if not courses:
        print("The course list empty, please add more course(s)!")
        return
    print("All courses list: ")
    for sId in courses:
        print(f"Course ID: {sId} \nStudent Name: {courses[sId]['name']}")

# Print the student mark
def markList():
    print(f"\nAll marks for the course {coursename}: ")
    for sId in students:
        print(f"Student name: {students[sId]['name']} \tMark: {students[sId]['marks'][coursename]}")

def main():
    while(True):
        i = int(input("""
-----------------------------------------
| Select one of these option:           |
| 1. Add student                        |
| 2. Add course                         |
| 3. Add mark                           |
| 4. Get student list                   |
| 5. Get course list                    |
| 6. Get student mark                   |
| 7. Exit                               |
-----------------------------------------\n"""))
        if i == 1:
            print("You have choosen the option 1: add student")
            studentNumber()
            studentInfo()
        elif i == 2:
            print("You have choosen the option 2: add course")
            courseNumber()
            courseInfo()
        elif i == 3:
            print("You have choosen the option 3: add mark")
            validationCourse()
            studentMark()
        elif i == 4:
            print("You have choosen the option 4: get the student list")
            studentList()
        elif i == 5:
            print("You have choosen the option 5: get the course list")
            courseList()
        elif i == 6:
            print("You have choosen the option 6: get the mark list")
            validationCourse()
            markList()
        elif i == 7:
            print("You have choosen the option 7: exit")
            break
        else:
            print("Invalid choice! Try again.")
            
if __name__ == "__main__":
    main() 
