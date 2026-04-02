from utils import GRADE_POINTS, check_valid_grade


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
        if len(self.get_courses()) == 0:
            return 0
        for course, grade in self.courses.items():
            course:Course #Typehint for IDE
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
        self.credits = int(credits) #makes sure it is int (Raises Error if not)
        self.students = []
        pass

    def add_student(self,student:Student):
        '''Adds student to list'''
        if student in self.students:
            raise ValueError("Student already in class.")
        self.students.append(student)
        

    def get_student_count(self) -> int:
        '''returns length of student list'''
        return len(self.students)
        

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

    def _load_csv(filepath):
        """Returns a 2d list [lines[lineinfo1, lineinfo2, ]]
        Gio
        """
        ret = []
        def mapper(a:str):
            """Returns a list of rows for the coulumn. Also removes the newline suffix."""
            a = a.removesuffix("\n")
            return a.split(",")
        
        with open(filepath, "r") as f:
            ret = list(map(mapper, f.readlines()))
        ret.pop(0)
        return ret

    @classmethod
    def from_csv(cls, univerity_data_path:str, course_catalog_path:str):
        """
        Gio
        Loads an instance of the university class from the given csv files
        """
        ret = cls()
        univerity_data = cls._load_csv(univerity_data_path)
        course_catalog = cls._load_csv(course_catalog_path)

        for c in course_catalog:
            ret.add_course(c[0], c[1])

        for l in univerity_data:
            s = ret.add_student(l[0], l[1])
            # course, grade in student_info[2]
            for i in l[2].split(";"):
                i = i.split(":")
                course = ret.get_course(i[0])
                if course is not None:
                    s.enroll(course, i[1])
                else:
                    print(f"Failed to enroll {s.name} in {course.course_code}")
        return ret

        
    pass
  