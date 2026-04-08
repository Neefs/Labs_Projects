from enum import Enum
from datetime import datetime

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
    ID = "id"
    NAME = "name"
    DATE = "date"


    

def bubble_sort(arr, by: CourseSortedBy):
    n = len(arr)
    # Outer loop for number of passes
    for i in range(n):
        # Inner loop for comparing adjacent elements
        for j in range(0, n - i - 1):
            # Compare adjacent strings alphabetically
            if by is CourseSortedBy.NAME:
                check = arr[j].student.name > arr[j + 1].student.name
            elif by is CourseSortedBy.ID:
                check = arr[j].student.student_id > arr[j + 1].student.student_id
            elif by is CourseSortedBy.DATE:
                check = arr[j].date > arr[j + 1].date
                
            if check:
                # Swap if the first string is "greater" than the second
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def insertion_sort(arr, by: CourseSortedBy):
    n = len(arr)

    for i in range(n):
        j = n - i - 1
        while (j < n - 1 \
                and (arr[j].student.name > arr[j+1].student.name\
                     if by is CourseSortedBy.NAME\
                        else arr[j].student.student_id > arr[j+1].student.student_id\
                            if by is CourseSortedBy.ID else\
                                arr[j].date > arr[j+1].date)):
            arr[j],arr[j+1] = arr[j+1], arr[j]
        j +=1
            
class Algorithms(Enum):
    BUBBLE = bubble_sort
    INSERTION = insertion_sort

def recursive_binary_search(l, target):
    if l == []:
        return False
    return _erbs(l, target, 0, len(l))
            

def _erbs(l, target: str, left: int, right: int) -> any | False: #Student instead of any (cant bc of circular input)
    """
    Returns Student object
    """
    if left >= right:
        return False
    median = (left + right) // 2
    print(l[median].student.student_id)
    if l[median].student.student_id == target:
        return l[median]
    if target < l[median].student.student_id:
        return _erbs(l, target, left, median)
    return _erbs(l, target, median+1, right)



