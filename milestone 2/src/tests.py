import unittest
from objects import Course, Student, University

class CourseTests(unittest.TestCase):
    """Gio"""
    def test_create(self):
        """Test the creation of a course object"""
        c_code = "CSE1010"
        c = Course(c_code, 3)
        self.assertEqual(c.course_code, c_code)
        self.assertEqual(c.credits, 3)
        self.assertEqual(c.students, [])

    def test_add(self):
        """Tests adding a student object the course object"""
        c = Course("CSE", 3)
        s = Student("STU123", "Jeff")
        c.add_student(s)
        self.assertEqual(c.get_student_count(), 1)
        self.assertEqual(c.students[0], s)

    def test_add_dupe(self):
        """Tests adding a duplicate student object the course object"""
        c = Course("CSE", 3)
        s = Student("STU123", "Jeff")
        c.add_student(s)
        with self.assertRaises(ValueError):
            c.add_student(s)    
        self.assertEqual(c.get_student_count(), 1)
        self.assertEqual(c.students[0], s)

    def test_student_count(self):
        """Tests to make sure the count is correct."""
        c = Course("CSE", 3)
        for i in range(10):
            s = Student(str(i), f"{i}-name")
            c.add_student(s)
            self.assertEqual(c.get_student_count(), i+1)
        self.assertEqual(c.get_student_count(), 10)

        
class StudentTests(unittest.TestCase):
    """Luke"""
    def test_init(self):
        t_id = "STU12345"
        t_name = "Student_25"
        s = Student(t_id, t_name)
        
        self.assertEqual(s.student_id, t_id)
        self.assertEqual(s.name, t_name)
        
    def test_enroll(self):
        '''Tests if student is enrolled'''
        s = Student("STU12345","Student_25")
        c = Course("CSE1010", 3)
        s.enroll(c,"A")
        
        self.assertIn(c, s.courses)
        self.assertEqual(s.courses[c], "A")
        
        self.assertIn(s, c.students)
        self.assertEqual(c.get_student_count(), 1)
        
        
    def test_gpa(self):
        '''Tests to make sure gpa calculation'''
        s = Student("STU12345","Student_25")
        c1 = Course("CSE1010", 3)
        c2 = Course("MATH010", 4)
        
        s.enroll(c1,"A")
        s.enroll(c2,"B")
        
        self.assertAlmostEqual(s.calculate_gpa(), 3.43, places=2)
        
    def test_get_courses(self):
        '''tests getting student courses'''
        s = Student("STU12345", "Student_25")
        c1 = Course("CSE1010", 3)
        c2 = Course("CSE2050", 3)
        
        s.enroll(c1, "A")
        s.enroll(c2, "B")
        
        course_list = s.get_courses()
        self.assertEqual(len(course_list), 2)
        self.assertIn(c1, course_list)
        self.assertIn(c2, course_list)




class UniversityTests(unittest.TestCase):
    """Gio"""
    def test_creation(self):
        """Test the creation of the university object"""
        u = University()
        self.assertEqual(u.courses, {})
        self.assertEqual(u.students, {})

    def test_add_course(self):
        """Tests adding a course to the university object"""
        u = University()
        c = u.add_course("CSE1010", 3)
        self.assertEqual(c.course_code, "CSE1010")
        self.assertEqual(c.credits, 3)
        self.assertEqual(u.get_course("CSE1010"), c)

    def test_add_course_dupe(self):
        """Tests adding a duplicate course to the university object"""
        u = University()
        c1 = u.add_course("CSE1010", 3)
        c2 = u.add_course("CSE1010", 3)
        self.assertEqual(id(c1), id(c2))
        self.assertEqual(len(u.courses), 1)

    def test_add_student(self):
        """Tests adding a student to the university object"""
        u = University()
        s = u.add_student("STU123", "John Doe")
        self.assertEqual(s.student_id, "STU123")
        self.assertEqual(s.name, "John Doe")
        self.assertEqual(u.get_student("STU123"), s)

    def test_add_student_dupe(self):
        """Tests adding a duplicate student to the university object"""
        u = University()
        s1 = u.add_student("STU123", "John Doe")
        s2 = u.add_student("STU123", "John Doe")
        self.assertEqual(id(s1), id(s2))
        self.assertEqual(len(u.students), 1)

    def test_get_student_info(self):
        """Tests getting student info from the university object"""
        u = University()
        s = u.add_student("STU123", "John Doe")
        self.assertEqual(u.get_student("STU123"), s)
        self.assertEqual(type(u.get_student("STU123")), Student)

    def test_get_student_info_not_found(self):
        """Tests getting student info that doesn't exist from the university object"""
        u = University()
        self.assertEqual(u.get_student("STU999"), None)

    def test_get_course_info(self):
        """Tests getting course info from the university object"""
        u = University()
        c = u.add_course("CSE1010", 3)
        self.assertEqual(u.get_course("CSE1010"), c)
        self.assertEqual(type(u.get_course("CSE1010")), Course)

    def test_get_course_info_not_found(self):
        """Tests getting course info that doesn't exist from the university object"""
        u = University()
        self.assertEqual(u.get_course("CSE999"), None)

unittest.main()