import unittest
from objects import Course, Student, University

class CourseTests(unittest.TestCase):
    def test_create(self):
        """Test the creation of a course object"""
        c_code = "CSE1010"
        c = Course(c_code, 3)
        self.assertEqual(c.course_code, c_code)
        self.assertEqual(c.credits, 3)
        self.assertEqual(c.students, [])
        
class StudentTests(unittest.TestCase):
    def test_init(self):
        t_id = "STU12345"
        t_name = "Student_25"
        s = Student(t_id,t_name)
        
        self.assertEqual(s.student_id,t_id)
        self.assertEqual(s.name,t_name)
        
    def test_enroll(self):
        s = Student("STU12345","Student_25")
        c = Course("CSE1010", 3)