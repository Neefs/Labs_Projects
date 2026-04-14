from __future__ import annotations
#Gio = Giovanni Ventura
#Luke = Luke Dopman

from objects import University, Student, Waitlist

if __name__ == "__main__":
    u = University.from_csv("milestone 2/enrollments_CSE10.csv", "milestone 2/course_catalog_CSE10_with_capacity.csv")
    print(u.students)
    for c in u.courses.values():
        print(c.enrollmentRecords, len(c.waitlist))
    # a = 0.0
    # for s in u.students.values():
    #     a += s.calculate_gpa()
    #     print(s.name)
    #     print(f"{s.calculate_gpa():.3f}")
    # print(f"Average GPA: {a / len(u.students):.3f}")


    # students = [Student("1", "a"), Student("2", "b"), Student("3", "c")]
    # q = Waitlist()
    # for s in students:
    #     q.enqueue(s)
    # print(q.dequeue().name)  
    # q.enqueue(students[0]) 
    # for i in range(len(q)):
    #     print(q.dequeue().name)

    #print(q.dequeue())