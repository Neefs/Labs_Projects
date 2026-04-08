from datetime import datetime
from typing import Literal
from utils import *
import time


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
        

class EnrollmentRecord:
    def __init__(self, student: Student, date: datetime | str = datetime.now()):
        self.student = student
        self.date = datetime.fromisoformat(date) if type(date) == str else date




    
class Course:
    '''Luke + Gio'''
    def __init__(self, course_code:str, name:str, credits:int, department:str, capacity: int):
        '''Initialize'''
        self.course_code = course_code
        self.credits = int(credits) #makes sure it is int (Raises Error if not)

        self.enrollmentRecords: list[EnrollmentRecord] = []
        self.name: str = name
        self.department:str = department
        self.capacity:int = capacity
        self.sortedBy: CourseSortedBy | None = None

        self.waitlist = Waitlist() #Add a waitlist object here.


    def enroll(self, student:Student, enroll_date:datetime | str = None):
        if any(er.student == student for er in self.enrollmentRecords):
            return 
        if len(self.enrollmentRecords) < self.capacity:
            if not enroll_date:
                enroll_date = datetime.now()
            self.enrollmentRecords.append(EnrollmentRecord(student, enroll_date))
            self.sortedBy = None #Adding the student breaks the sort so we set this to None
        else:
            self.waitlist.enqueue(student)
        # TODO: Return something here to tell if they were added to the waitlist or the course.
    
    def drop(self, student_id:str, enroll_date:datetime=None):
        if not (self.sortedBy is CourseSortedBy.ID):
            self.sort_enrolled(CourseSortedBy.ID)
            print("EnrollmentRecords are now sorted by ID to complete the drop.")
            #raise LookupError("Data has to be sorted by ID to drop this student.")
            # Possibly auto sort here
            
        dropped_student = recursive_binary_search(self.enrollmentRecords, student_id)
        if dropped_student is False:
            raise ValueError("Student could not be found.")
        self.enrollmentRecords.remove(dropped_student)
        if not self.waitlist.is_empty():
            new_student = self.waitlist.dequeue() 
            if enroll_date is None: enroll_date = datetime.now()
            self.enrollmentRecords.append(EnrollmentRecord(new_student, enroll_date))
            self.sort_enrolled(self.sortedBy) # Sorts by ID again
            #sortedBy will always be CourseSortedBy.ID at this point.

    

    def sort_enrolled(self, by: CourseSortedBy, algorithm: Algorithms = Algorithms.INSERTION):
        """Automaticly uses insertion because it is more efficient"""
        # Use (by is CourseSortedBy.ID) to see which one was called
        algorithm(self.enrollmentRecords, by) #Algorithms is an enum with the value being the function it is named after
        #since we store it as bubble_sort and not bubble_sort() we can call it.
        self.sortedBy = by
        #set sortedby
        


    
            





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


class WaitlistNode:
    def __init__(self, student: Student):
        self.student = student
        self.next: WaitlistNode | None = None


class Waitlist:
    def __init__(self):
        self._head: WaitlistNode = None
        self._tail: WaitlistNode = None
        self._len: int = 0


    def __len__(self):
        return self._len
    
    def is_empty(self):
        return self._head == None and self._tail == None and self._len == 0
    
    def enqueue(self, student:Student):
        node = WaitlistNode(student)
        
        print(self.is_empty())
        if self.is_empty():
            self._head = node 
            self._tail = node
            self._len += 1
            print("Enqued single")
            return
        self._tail.next = node
        self._tail = node
        self._len += 1

    def dequeue(self):
        if self.is_empty():
            raise ValueError("The Queue is empty")
        print("false", self._head, self._tail, self._len)
        ret = self._head
        if len(self) <= 1:
            self._head = None
            self._tail = None
        else:
            self._head = self._head.next
        self._len -= 1
        return ret.student




if __name__ == "__main__":
    students = [EnrollmentRecord(Student("STU00001","James"), ),EnrollmentRecord(Student("STU00002", "Gio")), EnrollmentRecord(Student("STU00003","Luke"))]
    time.sleep(3)
    students.append(EnrollmentRecord(Student("STU00004","yerp"), datetime.now()))
    sort = insertion_sort
    sort(students, CourseSortedBy.NAME)
    print([s.student.name for s in students])
    sort(students, CourseSortedBy.DATE)
    sort(students, CourseSortedBy.NAME)
    print([s.date for s in students])
    sort(students, CourseSortedBy.ID)
    print([s.student.student_id for s in students])