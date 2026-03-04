# CSE2050 Milestone 1
*University managment tool*

## main.py
*As module*
1. Import the module into your python file.
2. Initialize the University class using Univerity() or Univeristy.from_csv()
3. From there follow the documentation of the functions to use the module.

*As File*
* Run the python file using `python3 main.py`
* It will loop through the students and their gpas then give you a calculation for the average gpa of the Univerity (2.731)

## tests.py
* Run the tests.py file by doing `python3 tests.py`
* Should run 17 OK tests on the main module.


## Loading from CSV
As a requirement of this lab we had to load the univerity data from a csv. You can do this by doing:
```py
u = Univerity.from_csv("the/path/to/univeristiydata.csv", "the/path/to/course_catalog.csb")
```
This uses a classmethod to create the univerity class already populated.