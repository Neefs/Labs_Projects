import unittest

def find_sum_even(x, y):
    
    x = x if x%2 == 0 else x+1
    res = 0
    for i in range(x, y+1, 2):
        res += i
    return res


print(find_sum_even(1, 12))
# Runtime of O(n) 

def print_max(l:list):
    l=set(l) #Duplicates aren't needed 
    lmax = -1
    for i in l:
        if i > lmax and i < 10:
            lmax = i
    return lmax if lmax > -1 else None


class Tests(unittest.TestCase):
    def test_print_max(self):
        self.assertEqual(print_max([11, 12, 13]), None)
        self.assertEqual(print_max([]), None)
        self.assertEqual(print_max([9, 11, 12, 13]), 9)
        self.assertEqual(print_max([1, 11, 12, 13]), 1)
        self.assertEqual(print_max([-3, 1, 3, 5, 11, 12, 13]), 5)


unittest.main()


class Person:
    def __init__(self, first_name:str, last_name:str, age:int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def get_full_name(self) -> str:
        return self.first_name + " " + self.last_name
    
    def get_age(self) -> int:
        return self.age
    

class Employee(Person):
    def __init__(self, first_name:str, last_name:str, age:int, salary:float):
        super().__init__(first_name, last_name, age)
        self.salary = salary

    def get_employee_info(self) -> str:
        return self.get_full_name + " Age: " + self.get_age() + " Salary: " + self.salary
    
    def update_salary(self, newsalary:float) -> None:
        self.salary = newsalary

        