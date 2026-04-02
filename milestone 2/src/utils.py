from enum import Enum


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