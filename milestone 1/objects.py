
#Gio = Giovanni Ventura
#Luke = Luke Dopman

GRADE_POINTS = {
    'A' : 4.0, 'A-' : 3.7,
    'B+': 3.3, 'B' : 3.0, 'B-' : 2.7,
    'C+': 2.3, 'C' : 2.0, 'C-' : 1.7,
    'D' : 1.0,
    'F' : 0.0
}

def check_valid_grade(grade:str) -> bool:
    """Checks to see if the grade is valid
        Gio"""
    return GRADE_POINTS.get(grade) is not None

class Student:
    """Gio"""
    def __init__(self, student_id:str, name:str,):
        """Inititlizes the student class"""
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enroll(self, course:Course, grade:str):
        """Enrolls a student into the class. Adds self to courses students"""
        if not check_valid_grade(grade):
            raise AttributeError("Grade has to be a valid grade type.")
        self.courses[course] = grade
        course.add_student(self)

    def update_grade(self, course:Course, grade:str):
        """Updates the student grade. Throws error if grade is not valid"""
        if not check_valid_grade(grade):
            raise AttributeError("Grade has to be a valid grade type.")
        if self.courses.get(course):
            self.courses[course] = grade
        else:
            raise AttributeError("Course not enrolled in")
        
    def calculate_gpa(self):
        """Calculates a student's gpa"""
        total_grade_points = 0.0
        total_credits = 0
        for course, grade in self.courses.items():
            course:Course
            total_grade_points += (GRADE_POINTS[grade]*float(course.credits))
            total_credits += course.credits
        return total_grade_points/total_credits
    
    def get_courses(self):
        """Returns a list of courses"""
        return list(self.courses.keys())
    
    def get_course_info(self):
        """Prints course info as course_code/grade/credits"""
        for course, grade in self.courses.items():
            print(f"{course.course_code}\t{grade}\t{course.credits}")
        

    

    
class Course:
    '''Luke'''
    def __init__(self, course_code:str, credits:int):
        '''Initialize'''
        self.course_code = course_code
        self.credits = credits
        self.students = []
        pass

    def add_student(self,student:Student):
        '''Adds student to list'''
        self.students.append(student)
        pass

    def get_student_count(self) -> int:
        '''returns length of student list'''
        return len(self.students)
        pass

class University: 
    '''Luke'''
    def __init__(self):
        '''initailize'''
        self.courses = {}
        self.students = {}
    
    def add_course(self,course_code, credits):
        '''checks if course exsits, adds it and returns course object'''
        if course_code not in self.courses:
            self.courses[course_code] = Course(course_code,credits)
        return self.courses[course_code]
        
    def add_student(self,student_id, name) -> Student | None:
        '''check if student exists, adds it and returns student object'''
        if student_id not in self.students:
            self.students[student_id] = Student(student_id,name)
        return self.students[student_id]
        
    def get_student(self,student_id):
        """returns student object associated with student id"""
        return self.students.get(student_id)
        
    def get_course(self,course_code):
        """returns the course object associated with the course code"""
        return self.courses.get(course_code)
        
    def get_course_enrollment(self,course_code):
        """checks if course exists and returns the student count in the course, else None"""
        if self.courses.get(course_code):
            return self.courses[course_code].get_student_count()
        else:
            return None
        
    def get_students_in_course(self,course_code):
        """checks if course exists and returns the students in the course, else None"""
        if self.courses.get(course_code):
            return self.courses[course_code]
        else: None
        
    pass

def load_csv(filepath):
    """Returns a 2d list [lines[lineinfo1, lineinfo2, ]]
        Gio
    """
    ret = []
    def mapper(a:str):
        a = a.removesuffix("\n")
        return a.split(",")
    
    with open(filepath, "r") as f:
        ret = list(map(mapper, f.readlines()))
    ret.pop(0)
    return ret
    
if __name__ == "__main__":
    load_csv("milestone 1/course_catalog.csv")
    load_csv("milestone 1/university_data.csv")