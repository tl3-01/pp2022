import datetime
class student:
    def __init__(self, sId, name, DoB)
        self.__id = sId
        self.__name = name
        self.__DoB = DoB
        
    """ validation """
    def _checkId(self,sId):
        while True:
            try:
                idNum = int(self.idNum);
                if idNum < 0:
                    print("The ID number can't be negative! Try again.")
                elif len(str(idNum)) != 3:
                    print("The ID number is 3 digits! Try again.")
                elif str(idNum) == '000':
                    print("The ID number can't be all 0s! Try again.")
                else:
                    break
            except ValueError:
                print("The ID number must be a number! Try again.")
        
    def _checkName(self,name):
        while True:
            self.name = input("Please input student name: ")
            if not re.match(r'[a-zA-Z\s]+$', self.name):
                print ("Error! Make sure you only use letters in the student nam.")
            else:
                break
        
    def _checkDoB(self,DoB)
        while True:
            self.DoB = input("Please input student dob: ")
            try:
                dob = datetime.datetime.strptime(self.DoB,"%d/%m/%Y").date()
            except ValueError:
                print("Wrong format for DoB! Try again.")
            else:
                break
        
    """ getter """
    @property
    def sId(self)
        return self.__id

    @property
    def name(self):
        return self.__name
    
    @property
    def DoB(self):
        return self.__DoB

    
    """ setter """
    @sId.setter
    def sId(self, value):
        self._checkId(value)
        self.__id = value
    
    @name.setter
    def name(self, value):
        self._checkName(value)
        self.__name = value
        
    @DoB.setter
    def DoB(self, value):
        self._checkDoB(value)
        self.__DoB = value
    
    def __str__(self):
        return '{} - {} - {}'.format(self.sId, self.name, self.DoB)

class course:
    def __init__(self, sId, name)
        self.__id = sId
        self.__name = name
        
    """ validation """
    def _checkId(self,sId):
        while True:
            try:
                course_id = int(self.sId)
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
        
    def _checkName(self,name):
        while True:
            if not re.match(r'[a-zA-Z\s]+$', self.name):
                print ("Error! Make sure you only use letters in the student name.")
            else:
                break
        
    """ getter """
    @property
    def sId(self)
        return self.__id

    @property
    def name(self):
        return self.__name
    
    """ setter """
    @sId.setter
    def sId(self, value):
        self._checkId(value)
        self.__id = value
    
    @name.setter
    def name(self, value):
        self._checkName(value)
        self.__name = value
        
    @DoB.setter
    def DoB(self, value):
        self._checkDoB(value)
        self.__DoB = value
    
    def __str__(self):
        return '{} - {}'.format(self.sId, self.name)
    
class studentList:
    def checkStudent(self, studentNum):
        while True:
            try:
                student_num = int(self.studentNum)
                if student_num < 0:
                    print("The number of students can't be negative! Try again.")
                elif student_num == 0:
                    print("The number of students can't be equal to 0! Try again.")
            except ValueError:
                print("The number of students must be a number! Try again.")
            else:
                break
    def __init__(self)
        self._sList = list(student)
    def input(self):
        student_num = input('Enter the number of students in a class: ')
        try:
            self.checkStudent(student_num)
        else:
            break
        for i in range(student_num)
            sId =int(input("Please input student ID:"))
            name = input("Please input student name:")
            DoB = input("Please input student DoB:")
            self._sList.append(student(sId, name, DoB))
    def list(self):
        print(_sList)
    
class courseList:
    def checkCourse(self, courseNum):
        while True:
            try:
                course_num = int(self.courseNum)
                if course_num < 0:
                    print("The number of courses can't be negative! Try again.")
                elif course_num == 0:
                    print("The number of courses can't be equal to 0! Try again.")
            except ValueError:
                print("The number of courses must be a number! Try again.")
            else:
                break
    def __init__(self)
        self._cList = list(course)
    def input(self):
        course_num = input('Enter the number of courses in a class: ')
        try:
            self.checkStudent(course_num)
        else:
            break
        for i in range(course_num)
            sId =int(input("Please input course ID:"))
            name = input("Please input course name:")
            self._cList.append(course(sId, name))
    def list(self):
        print(_cList)
        
class Mark(student):
    def __init__(self, sId, name, DoB, mark):
        super().__init__(sId, name, DoB)
        self.mark = []
    def inputMark(self,mark):
        while True:
            courseNameCheck = input("Please enter course name")
            for course in courseList._cList:
