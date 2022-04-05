import datetime
import re
class students:
    def __init__(self):
        self.__sId = ''
        self.__name = ''
        self.__DoB = ''

    """ input and validate """
    def input_id(self):
        self.prefix = ''
        while True:
            prefix = input("Please enter one of the prefix \"BI11\" or \"BA10\" for the student ID: ")
            if prefix not in {"BI11", "BA10"}:
                print("The prefix must be \"BI11\" or \"BA10\". Try again!")
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
        self.__sId = prefix + "-" + str(idNumber)
        return self.__sId
    
    def input_name(self):
        while True:
            name = input("Please input student name: ")
            if not re.match(r'[a-zA-Z\s]+$', name):
                print ("Error! Make sure you only use letters in the student name.")
            else:
                return self.__name
        
    def input_DoB(self):
        while True:
            DoB = input("Please input student DoB (Input format: dd/mm/yyyy): ")
            try:
                dob = datetime.datetime.strptime(DoB,"%d/%m/%Y").date()
            except ValueError:
                print("Wrong format for DoB! Try again.")
            else:
                return self.__DoB

    """ getter """
    @property
    def sId(self):
        return self.__sId

    @property
    def name(self):
        return self.__name
    
    @property
    def DoB(self):
        return self.__DoB
    
    # """ setter """
    # @sId.setter
    # def sId(self, sId, prefix, idNumber):
    #     self.__input_id(sId, prefix, idNumber)
    #     self.__sId = sId
    #
    # @name.setter
    # def name(self, name):
    #     self.__input_name(name)
    #     self.__name = name
    #    
    # @DoB.setter
    # def DoB(self, DoB):
    #     self.__input_DoB(DoB)
    #     self.__DoB = DoB
    
class courses:
    def __init__(self):
        super().__init__()
        self.__id = 0
        self.__name = ''
        
    """ validation """
    def __input_id(self, sId):
        while True:
            self.sId = input(f"\nPlease enter the course Id: ")
            try:
                course_id = int(self.sId)
                if course_id < 0:
                    print("The ID number can't be negative! Try again.")
                elif len(str(course_id)) != 2:
                    print("The ID number is 2 digits! Try again.")
                elif str(course_id) == '000':
                    print("The ID number can't be all 0s! Try again.")
                else:
                    return self.__sId
            except ValueError:
                print("The ID number must be a number! Try again.")
        
    def __check_name(self, name):
        while True:
            if not re.match(r'[a-zA-Z\s]+$', self.name):
                print ("Error! Make sure you only use letters in the student name.")
            else:
                return self.__name
        
    """ getter """
    @property
    def sId(self):
        return self.__id

    @property
    def name(self):
        return self.__name
    
    # """ setter """
    # @sId.setter
    # def sId(self, sId):
    #     self.__check_id(sId)
    #     self.__id = sId
    # 
    # @name.setter
    # def name(self, name):
    #     self.__check_name(name)
    #     self.__name = name
    
    def __str__(self):
        return '{} - {}'.format(self.sId, self.name)
    
class studentList:
    def __init__(self):
        self.__student_num = 0
        self.__students = {}
    """getter"""
    @property
    def student_num(self):
        return self.__student_num
    
    def input_student_num(self):
        while True:
            student_num = input('Enter the number of students in a class: ')
            try:
                student_num = int(student_num)
                if student_num <= 0:
                    print("The number of students must be positive. Try again!")
                    continue
            except ValueError:
                print("The number of students must be a number! Try again.")
            else:
                self.__student_num = student_num
                return self.__student_num
            
    def input_student(self):
        for i in range(self.input_student_num()):
            print(f"\n--- Input the data for student {i+1} ---")
            sId = students().input_id()
            name = students().input_name()
            DoB = students().input_DoB()
            self.__students[sId] = {
                "name": name,
                "DoB": DoB,
                "marks" : {}
            }
        return self.__students[sId]
    @property
    def students(self):
        return self.__students
    
    def __str__(self):
        return f"{self.__students}"

class courseList(courses):
    def __init__(self):
        self.__course_num = 0
    
    def input_course_num(self):
        while True:
            self.__course_num = input('Enter the number of courses: ')
            try:
                course_num = int(self.__course_num)
                if course_num <= 0:
                    print("The number of students must be positive. Try again!")
                    continue
            except ValueError:
                print("The number of courses must be a number! Try again.")
            else:
                return self.__course_num
    
    def input_course(self):
        for i in range(self.__course_num):
            print(f"\n--- Input the data for course {i+1} ---")
            sId = self.__input_id()
            name = self.__input_name()
            self.__courses.append(sId, name)
     
    """getter"""
    @property
    def course_num(self):
        return self.__course_num
    
    @property
    def courses(self):
        return self.__courses
    
    def __str__(self):
        return f"Student ID: {self.__sId} \nStudent Name: {self.__name}"

class markList(studentList):
    def __init__(self):
        super().__init__()
        self.__marks = {}
        
    def validation_course(self, coursename):
        if not courses.__courses:
            print("The course list empty, please add more course(s)!")
            return
        elif not students.__students:
            print("The student list empty, please add more student(s)!")
            return
        for sId in courses:
            while True:
                if coursename == courses['name']:
                    print(f"The course {coursename} is in course list, please continue.")
                    return coursename
                else:
                    print(f"The course {coursename} is not in course list. Try again!")
                    continue
                     
    @property
    def marks(self):
        return self.__marks  
    
    def input_mark(self, mark, coursename):
        while True:
            self.mark = input(f"- Student {self.__name}: ") 
            try:
                mark = float(mark)
                if mark > 20.0 or mark < 0.0:
                    print("The mark must be between 0 and 20. Try again!")
                else:
                    self.__marks[coursename] = mark
                    return self.__marks[coursename]
            except ValueError:
                print("Wrong data type for mark. Try again!")
            
    def __str__(self):
        return f"Student name: {student.__sId} \tMark: {self.__marks[coursename]}"
                
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
            studentList().input_student()
        elif i == 2:
            print("You have choosen the option 2: add course")
            courseList().input_course_num()
            courseList().input_course()
        elif i == 3:
            print("You have choosen the option 3: add mark")
            markList().validation_course()
            markList().input_mark()
        elif i == 4:
            print("You have choosen the option 4: get the student list")
            print(studentList().__str__())
        elif i == 5:
            print("You have choosen the option 5: get the course list")
            courseList().__str__()
        elif i == 6:
            print("You have choosen the option 6: get the mark list")
            markList().__str__()
        elif i == 7:
            print("You have choosen the option 7: exit")
            break
        else:
            print("Invalid choice! Try again.")
            
if __name__ == "__main__":
    main() 
    