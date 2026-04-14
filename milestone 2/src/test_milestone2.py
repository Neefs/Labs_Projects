import unittest
from objects import *
from utils import *

class QueueTests(unittest.TestCase):
    """Gio"""
    def test_FIFO(self):
        """checks first in first out"""
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
        """test empty dequeue"""
        wl = Waitlist()
        self.assertRaises(ValueError, wl.dequeue)
        
    def test_size_tracking(self):
        """test if sie tracking is working"""
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
    """Luke"""
    def setUp(self):
        """works as initializer for rest of testcase by adding students to test on"""
        self.course = Course("CSE000","Name",3, "department", capacity = 2)
        self.s1 = Student("STU00001","James")
        self.s2 = Student("STU00002", "Gio")
        self.s3 = Student("STU00003","Luke")

    def test_capacity(self):
        """tests capacity"""
        self.course.enroll(self.s1)
        self.course.enroll(self.s2)

        self.assertEqual(len(self.course.enrollmentRecords),2)

        self.course.enroll(self.s3)
        self.assertEqual(len(self.course.enrollmentRecords),2)
        self.assertEqual(len(self.course.waitlist),1)

    def test_drop(self):
        """test if drop works"""
        self.course.enroll(self.s1)
        self.course.enroll(self.s2)
        self.course.enroll(self.s3)
        self.course.sort_enrolled(CourseSortedBy.ID, Algorithms.INSERTION)

        self.course.drop(self.s1.student_id)
        self.assertEqual(len(self.course.enrollmentRecords),2)
        self.assertEqual(len(self.course.waitlist),0)



class test_sort(unittest.TestCase):
    """Luke"""
    def setUp(self):
        """works as intializer by creating course, students, and enrolling them"""
        self.course = Course("CSE000","Name",3, "department", capacity = 4)
        self.s1 = Student("STU00001","James")
        self.s2 = Student("STU00002", "Gio")
        self.s3 = Student("STU00003","Luke")
        self.course.enroll(self.s1, "2022-10-20")
        self.course.enroll(self.s3, "2021-01-03")
        self.course.enroll(self.s2, "2020-03-13")
        

    def test_bubble_name(self):
        """test bubble sort with names"""
        self.course.sort_enrolled(CourseSortedBy.NAME,Algorithms.BUBBLE)
        names = list(map(lambda er: er.student.name ,self.course.enrollmentRecords))
        self.assertEqual(names, ["Gio", "James", "Luke"])

    def test_insert_name(self):
        """test insertion sort with names"""
        self.course.sort_enrolled(CourseSortedBy.NAME,Algorithms.INSERTION)
        names = list(map(lambda er: er.student.name ,self.course.enrollmentRecords))
        self.assertEqual(names, ["Gio", "James", "Luke"])

    
    def test_bubble_id(self):
        """test bubble sort for ids"""
        self.course.sort_enrolled(CourseSortedBy.ID,Algorithms.BUBBLE)
        ids = list(map(lambda er: er.student.student_id ,self.course.enrollmentRecords))
        self.assertEqual(ids, ["STU00001", "STU00002", "STU00003"])

    def test_insert_id(self):
        """test insertion sort for ids"""
        self.course.sort_enrolled(CourseSortedBy.ID,Algorithms.INSERTION)
        ids = list(map(lambda er: er.student.student_id ,self.course.enrollmentRecords))
        self.assertEqual(ids, ["STU00001", "STU00002", "STU00003"])

    def test_bubble_dates(self):
        """tests bubble sort for the dates"""
        self.course.sort_enrolled(CourseSortedBy.DATE,Algorithms.BUBBLE)
        dates = list(map(lambda er: er.date, self.course.enrollmentRecords))
        self.assertEqual(dates, [datetime.fromisoformat("2020-03-13"),datetime.fromisoformat("2021-01-03"),datetime.fromisoformat("2022-10-20") ])

    def test_insert_dates(self):
        """tests insertion sort for dates"""
        self.course.sort_enrolled(CourseSortedBy.DATE,Algorithms.INSERTION)
        dates = list(map(lambda er: er.date ,self.course.enrollmentRecords))
        print(dates)
        self.assertEqual(dates, [datetime.fromisoformat("2020-03-13"),datetime.fromisoformat("2021-01-03"),datetime.fromisoformat("2022-10-20") ])

        
        

class BinarySearchTests(unittest.TestCase):
    """Gio"""
    def setUp(self):
        """works as initalizer by creating course and 3 students"""
        self.course = Course("CSE000","Name",3, "department", capacity = 3)
        self.s1 = Student("STU00001","James")
        self.s2 = Student("STU00002", "Gio")
        self.s3 = Student("STU00003","Luke")

    def test_not_found(self):
        #using drop because that is when we call binary search
        with self.assertRaises(ValueError) as cm:
            self.course.drop("STUDOESNOTEXIST")
            #BS return False
            #Drop raises value error when bs is false (student not found)
    
    def test_find_first(self):
        """tests if the first is found"""
        self.course.enroll(self.s1)
        self.course.enroll(self.s2)
        self.course.enroll(self.s3)
        ds1 = self.course.drop(self.s1.student_id)[0]
        self.assertEqual(ds1, self.s1)

    def test_find_middle(self):
        """tests if the middle was found"""
        self.course.enroll(self.s1)
        self.course.enroll(self.s2)
        self.course.enroll(self.s3)
        ds1 = self.course.drop(self.s2.student_id)[0]
        self.assertEqual(ds1, self.s2)

    def test_find_last(self):
        """tests if last was found"""
        self.course.enroll(self.s1)
        self.course.enroll(self.s2)
        self.course.enroll(self.s3)
        ds1 = self.course.drop(self.s3.student_id)[0]
        self.assertEqual(ds1, self.s3)


class ExtraCreditTests(unittest.TestCase):
    """Gio
    checks for duplicate"""
    def test_double_waitlist_enrollment(self):
        c = Course("CSE000","Name",3, "department", capacity = 1)
        s1 = Student("STU00001","James")
        s2 = Student("STU00002", "Gio")

        c.enroll(s1)
        c.enroll(s2)
        self.assertEqual(c.get_student_count(), 1)
        self.assertEqual(len(c.waitlist), 1)
        with self.assertRaises(ValueError) as e:
            c.enroll(s2) 



    
        
        
        

    

unittest.main()