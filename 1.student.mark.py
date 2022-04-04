import re
import datetime
students = {
    "id" : None,
    "name" : None,
    "DoB" : None,
    "mark" : {}
}
courses = {
    "course_id" : None,
    "name" : None
}
list_course = []
list_student = []
# Input number of students
def student_number():
    global student_num
    while True:
        student_num = input('Enter the number of students in a class: ')
        try:
            student_num = int(student_num)
            if student_num < 0:
                print("The number of students can't be negative! Try again.")
            elif student_num == 0:
                print("The number of students can't be equal to 0! Try again.")
        except ValueError:
            print("The number of students must be a number! Try again.")
        else:
            break
        return student_num
    
# Input number of courses
def course_number():
    global course_num
    while True:
        course_num = input('Enter the number of courses: ')
        try:
            course_num = int(course_num)
            if course_num < 0:
                print("The number of courses can't be negative! Try again.")
            elif course_num == 0:
                print("The number of courses can't be equal to 0! Try again.")
        except ValueError:
            print("The number of courses must be a number! Try again.")
        else:
            break
        return course_num
    
# Get student ID, name, dob
def student_info():
    for i in range(0, student_num):
        prefix = ''
        while True:
            prefix = input("Please enter one of the prefix \"BI11\" or \"BA10\" for the student ID: ")
            if prefix not in {"BI11", "BA10"}:
                print("The prefix must be \"BI11\" or \"BA10\"")
            else:
                break
        while True:
            id_number = input("Please input last 3 digits of student ID: ")
            try:
                id_number = int(id_number);
                if id_number < 0:
                    print("The ID number can't be negative! Try again.")
                elif len(str(id_number)) != 3:
                    print("The ID number is 3 digits! Try again.")
                elif str(id_number) == '000':
                    print("The ID number can't be all 0s! Try again.")
                else:
                    break
            except ValueError:
                print("The ID number must be a number! Try again.")
        students['id'] = prefix + "-" + str(id_number)
        
        while True:
            students['name'] = input("Please input student name: ")
            if not re.match(r'[a-zA-Z\s]+$', students['name']):
                print ("Error! Make sure you only use letters in the student name.")
            else:
                break

        while True:
            students["DoB"] = input("Please input student DoB (Input format: dd/mm/yyyy):")
            try:
                dob = datetime.datetime.strptime(students["DoB"],"%d/%m/%Y").date()
            except ValueError:
                print("Wrong format for DoB! Try again.")
            else:
                break
        list_student.append(students.copy())
        
# Get course id and name
def course_info():
    for i in range(0, course_num):
        while True:
            courses['course_id'] = input("Please input the course ID number: ")
            try:
                course_id = int(courses['course_id']);
                if course_id < 0:
                    print("The ID number can't be negative! Try again.")
                elif len(str(course_id)) != 2:
                    print("The ID number is 2 digits! Try again.")
                elif str(course_id) == '000':
                    print("The ID number can't be all 0s! Try again.")
                else:
                    break
            except ValueError:
                print("The ID number must be a number! Try again.")
        while True:
            courses['name'] = input("Please input course name: ")
            if not re.match(r'[a-zA-Z\s]+$', courses['name']):
                print ("Error! Make sure you only use letters in the course name.")
            else:
                break
        list_course.append(courses.copy())
        
# Select course and input the mark of students in this course
mark = ''
def student_mark(course):
    for i in range(len(list_student)):
        mark = input(f"Input mark for student ID {i+1} for course {course} :")
        list_student[i]['mark'][course] = mark

# Print the student list
# Print the course list
# Print the student mark

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
-----------------------------------------\n"""))
        if i == 1:
            student_number()
            student_info()
        elif i == 2:
            course_number()
            course_info()
        elif i == 3:
            for i in range(len(list_course)):
                print("This is all course names:",list_course[i]["name"])
            sub = input("Input the subject from course: ")
            student_mark(sub)
        elif i == 4:
            print(list_student)
        elif i == 5:
            print(list_course)
        else:
            print("Invalid choice! Try again.")
            
if __name__ == "__main__":
    main() 
