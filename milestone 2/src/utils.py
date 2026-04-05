from enum import Enum
from datetime import datetime
from objects import EnrollmentRecord

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

class CourseSortedBy(Enum):
    ID = "id",
    NAME = "name",
    DATE = "date"

def er_binary_serach(l, target):
    if l == []:
        return False
    return _erbs(l, target, 0, len(l))
            

def _erbs(l: list[EnrollmentRecord], target: str, left: int, right: int):
    if left > right:
        return False
    median = (left + right) // 2
    if l[median].student.student_id == target:
        return l[median]
    if l[median].student.student_id < target:
        return _bs(l, target, left, median)
    return _bs(l, target, median+1, right)

def binary_search(l: list, target: str):
    if l == []:
        return False
    return _bs(l, target, 0, len(l))
        

def _bs(l: list, target: str, left: int, right: int):
    if left > right:
        return False
    median = (left + right) // 2
    if l[median] == target:
        return True
    if l[median] < target:
        return _bs(l, target, left, median)
    return _bs(l, target, median+1, right)