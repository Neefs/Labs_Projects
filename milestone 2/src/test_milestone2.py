import unittest
from objects import *
from utils import *

class QueueTests(unittest.TestCase):
    def test_FIFO(self):
        wl = Waitlist()
        students = [Student("0", "Jeff"), Student("1", "Ann"), Student("2", "Joe")]
        for s in students:
            wl.enqueue(s)
        self.assertEqual(wl.dequeue(), students[0])
        wl.enqueue(students[0])
        self.assertEqual(wl.dequeue(), students[1])
        self.assertEqual(wl.dequeue(), students[2])
        self.assertEqual(wl.dequeue(), students[0])

    def test_empty_deq(self):
        wl = Waitlist()
        self.assertRaises(ValueError, wl.dequeue)
        
    def test_size_tracking(self):
        wl = Waitlist()
        students = [Student(str(i), str(i)+" name") for i in range(10)]
        for s in students:
            wl.enqueue(s)
            self.assertEqual(len(wl), students.index(s)+1)
        self.assertEqual(len(wl), len(students))
        for wls in range(len(wl), 0, -1):
            s = wl.dequeue()
            self.assertEqual(len(wl), wls-1)
        self.assertTrue(wl.is_empty())





class test_enrollment(unittest.TestCase):
    def setUp(self):
        self.course = Course("CSE000","Name",3, "department", capacity = 2)
        self.s1 = Student("STU00001","James")
        self.s2 = Student("STU00002", "Gio")
        self.s3 = Student("STU00003","Luke")

    def test_capacity(self):
        self.course.enroll(self.s1)
        self.course.enroll(self.s2)

        self.assertEqual(len(self.course.enrollmentRecords),2)

        self.course.enroll(self.s3)
        self.assertEqual(len(self.course.enrollmentRecords),2)
        self.assertEqual(len(self.course.waitlist),1)

    def test_drop(self):
        self.course.enroll(self.s1)
        self.course.enroll(self.s2)
        self.course.enroll(self.s3)
        self.course.sort_enrolled(CourseSortedBy.ID, Algorithms.INSERTION)

        self.course.drop(self.s1.student_id)
        self.assertEqual(len(self.course.enrollmentRecords),2)
        self.assertEqual(len(self.course.waitlist),0)

    

        
        

class BinarySearchTests(unittest.TestCase):
    pass
        

    

unittest.main()