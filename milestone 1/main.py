import objects


u = objects.University()

#add courses
for l in objects.load_csv("milestone 1/course_catalog.csv"):
    u.add_course(l[0], int(l[1]))

for l in objects.load_csv("milestone 1/university_data.csv"):
    s = u.add_student(l[0], l[1])
    # course, grade
    for i in l[2].split(";"):
        i = i.split(":")
        course = i[0]
        grade = i[1]
        course = u.get_course(course)
        if course is not None:
            s.enroll(course, grade)

for s in u.students.values():
    print(s.name)
    print(f"{s.calculate_gpa():.3f}")