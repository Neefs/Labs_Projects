```
CSE 2050 Data structures and Object-Oriented Design Spring 2026
```
```
Project Milestone #
```
# 1 Overview

In Milestone 2, you will extend your Milestone 1 University/Course/Student system with features that
directly connect to the next three modules: linear data structures, recursion, and sorting/searching.
Each course has a maximum enrollment capacity. When a course reaches capacity, additional enrollment
requests must go to a waitlist implemented as a Queue ADT using a linked list. When a seat opens (a student
drops), the next student on the waitlist is automatically enrolled.
You will also add the ability to sort the enrolled roster by studentid or name using multiple sorting
algorithms. Finally, when the roster is sorted by studentid, dropping a student must locate that student
using a recursively implemented binary search.

# 2 Learning Goals

- Implement a linked-list-based LinkedQueue and use it as a waitlist.
- Apply capacity rules and First In First Out (FIFO) waitlisting using a Queue ADT.
- Implement at least two sorting algorithms and use them to sort rosters by different keys.
- Implement recursive binary search and use it for efficient drop operations when the roster is sorted by
    ID.
- Write meaningful unit tests using unittest and explain time complexity.

# 3 Provided Data Files (Milestone 2)

You will be provided a CSE-only dataset (10 courses) to ensure the capacity and waitlist behavior can be
demonstrated clearly. Use the following files as inputs for your program and tests:

- coursecatalogCSE10withcapacity.csv — course catalog (CSE only) including capacity column.
- enrollmentsCSE10.csv — enrollment records for the CSE courses.

# 4 What You Should Modify vs. What You Should Add

- Reuse (from Milestone 1): Student, Course, University.
- Modify:
    - Course: add capacity from coursecatalogCSE10withcapacity.csv; add waitlist + sorting
       + drop behavior.
    - University: load the updated course catalog and connect enroll/drop operations to the correct
       course.
    - Student: minimal or no changes.
- Add: LinkedQueue (with Node), at least two sorting algorithms, and a recursive binary search function.

# 5 What You Must Build

Your system must support the following scenario:

- Each Course has a maximum capacity for enrolled students.


- Students who can enroll and there is available space are added directly to the enrolled roster with an
    enrollment date.
- Additional eligible students are added to a waitlist implemented as a linked-list Queue (FIFO).
- The enrolled roster can be sorted by student name, student ID, or enrollment date using different sorting
    algorithms.
- When the roster is sorted by student ID, dropping a student uses recursive binary search to locate the
    student quickly.
- When a student drops, the next student on the waitlist (if any) is dequeued and enrolled automatically.

# 6 Tasks and Requirements

## 6.1 Task 1 — EnrollmentRecord (store student + enrollment date)

Create an EnrollmentRecord structure to represent enrollment in a course.

- Fields: student (Student object) and enrolldate (either a datetime.date or a string in YYYY-MM-DD
    format).
- The Course enrolled roster must store EnrollmentRecord objects (not raw Student objects).
- Your sorting and searching functions must operate on EnrollmentRecord objects.

## 6.2 Task 2 — LinkedQueue ADT (waitlist)

Implement a queue using a linked list. Do NOT use Python’s list as the underlying storage.

- Implement a Node class with fields data and next.
- Required methods: enqueue(item), dequeue(), isempty(), len ().
- dequeue() must raise an exception (ValueError or custom) if the queue is empty.
- FIFO behavior must be correct.

## 6.3 Task 3 — Course capacity + waitlist logic

Update the Course class to support capacity and waitlist behavior.

- Add a capacity attribute to Course.
- Add an enrolled roster (list of EnrollmentRecord).
- Add a waitlist attribute of type LinkedQueue.
- Implement requestenroll(student, enrolldate):
    - If the student is already enrolled, handle it (ignore or raise — document your choice).
    - If there is space, add an EnrollmentRecord to the enrolled roster.
    - If full, enqueue the student onto the waitlist.
- Implement drop(studentid, enrolldateforreplacement=None):
    - Remove the student from the enrolled roster (see Task 5 for search).
    - If the waitlist is not empty, dequeue the next student and enroll them with a new enrollment date
       (use today’s date or the provided enrolldateforreplacement).

## 6.4 Task 4 — Sorting the enrolled roster

Implement sorting of the enrolled roster by different keys.

- Support sorting by: (1) student name, (2) student ID, (3) enrollment date.
- Implement at least two sorting algorithms from class (e.g., insertion sort and selection sort).
- Provide a method sortenrolled(by, algorithm) where by is one of: ’name’, ’id’, ’date’.
- Your sort must rearrange the enrolled roster of EnrollmentRecord objects.


- After sorting, the course must record what key it is currently sorted by (recommended: enrolledsortedby
    attribute).

## 6.5 Task 5 — Recursive binary search for drop (when sorted by ID)

Implement recursive binary search and use it to support dropping students by ID.

- Implement recursivebinarysearch(records, targetid, low, high) recursively (no loops inside
    this function).
- The binary search must operate over EnrollmentRecord objects sorted by student ID.
- If the enrolled roster is not currently sorted by ID, your drop() must either:
    - (A) re-sort by ID automatically, OR
    - (B) raise an exception with a clear error message.
- drop(studentid) must use recursivebinarysearch to locate the student and then remove them.

## 6.6 Task 6 — Unit tests (unittest)

Write unit tests to demonstrate correctness. Include a test file named testmilestone2.py.
Test it with your own data for enrollment dates and course capacity.

- LinkedQueue tests: FIFO order; dequeue on empty raises; size tracking.
- Enrollment tests: enroll until capacity; extra students go to waitlist; drop triggers waitlist promotion.
- Sorting tests: roster correctly sorted by id, name, and date for each algorithm you implement.
- Binary search tests: find first/middle/last; not found returns−1; (and/or) behavior when roster not
    sorted by ID.

## 6.7 Task 7 — Complexity reflection (short report)

Submit a short file named milestone2report.txt (about^12 page) that answers the below with explanations:

- Give Big-O time complexity for enqueue and dequeue in your LinkedQueue.
- Give Big-O time complexity for each sorting algorithm you implemented.
- Give Big-O time complexity for recursive binary search and explain why sorting is required for correctness.
- Briefly compare your two sorting algorithms: when might one be preferred?

# 7 Submission Checklist

- All Python source files for Milestone 2 (including LinkedQueue and EnrollmentRecord).
- testmilestone2.py with passing unittest cases.
- milestone2report.txt with complexity discussion.
- A short demo script (optional but recommended): demomilestone2.py that shows enrolling, waitlist,
    sorting, and dropping.

# 8 Completion Checkpoints (Lab Support)

During each lab, your TA will do a quick progress check based on the checkpoint items below. Come prepared
to show your code running (and tests if applicable) so the TA can verify your completion.

- Lab — 3/25 (Checkpoint 1: Capacity + Waitlist Foundation + Sorting + Drop + Re-
    cursive Search)
       - Milestone 1 codebase running with the CSE10 files loaded correctly (including course capacity).
       - A working linked-list LinkedQueue (Node, enqueue, dequeue, isempty, len ).


- The Course class updated with capacity and waitlist.
- Enrollment behavior: enroll until capacity; extra students go to the waitlist (FIFO).
- At least two sorting algorithms implemented and working.
- The enrolled roster can be sorted by studentid and by name.
- A recursive binary search implementation for finding a student by ID (when sorted by ID).
- Drop behavior: remove the student and promote the next waitlisted student (if any).
TA check: Show one course reaching capacity and at least 2 students placed on the waitlist. Sort by
ID, drop a student, and show the next waitlisted student is enrolled.
- Lab — 4/1 (Testing)
- A recursive binary search implementation for finding a student by ID (when sorted by ID).
- A complete unittest suite with passing tests (queue, waitlist, sorting, binary search/drop).
TA check: Run tests successfully.
- Lab — 4/8 (Submission Day: Final Packaging)
- All required functionality is complete and stable.
- The complexity report is complete, and the submission is packaged correctly.
TA check: Run a short demo showing the full workflow.


# 9 Grading Rubric (90 points)

```
Category What we look for Points
```
```
EnrollmentRecord implemented and used
in course roster
```
```
Correct fields; roster stores
EnrollmentRecord; sorting/search-
ing works over records.
```
### 10

```
LinkedQueue (linked-list implementation) Node + LinkedQueue; correct FIFO; er-
rors on empty; correct size tracking.
```
### 20

```
Course capacity + waitlist behavior Enroll up to capacity; overflow to wait-
list; drop promotes next waitlisted stu-
dent.
```
### 20

```
Sorting: keys and algorithms Sort by name/id/date; at least
2 algorithms; roster remains
EnrollmentRecord list; correct or-
dering.
```
### 10

```
Recursive binary search used for drop Binary search implemented recursively;
correct index/−1; used in drop when
sorted by ID; handles unsorted case.
```
### 10

```
Unit tests (unittest) Covers queue, enrollment/waitlist, sort-
ing, binary search; tests are meaningful
and pass.
```
### 10

```
Complexity report Correct Big-O; clear explanations; com-
parison of sorting algorithms; binary
search correctness condition.
```
### 5

```
Code quality and documentation Readable structure; meaningful names;
comments/docstrings where needed; fol-
lows course style guidelines.
```
### 5

```
Peer Evaluation Will be evaluated after milestone submis-
sion
```
### 10

# 10 Extra Credit (up to +5 points)

- Prevent duplicate students in waitlist and/or enrolled roster with clear behavior.
- Add an Undo feature for enroll/drop using a Stack ADT (and tests).

# 11 Academic Integrity and Collaboration

Follow the course collaboration policy. You may discuss ideas with classmates, but all code you submit must
be written by your group. Cite any external resources used (documentation, tutorials) in comments or in
your report.


