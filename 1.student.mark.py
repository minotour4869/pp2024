def get_number_of_students():
    while True:
        try:
            num_student = int(
                input("Input number of students in your class: "))
            if num_student > 0:
                return num_student
            raise ValueError("Students number cannot below zero")
        except ValueError as val:
            print(val)
        except Exception as e:
            print(f"Unexpected {e=}: {type(e)=}")
        finally:
            print()


def get_student_information(student_id):
    print(f"\nInfo for student number {student_id}:")

    def get_student_id():
        while True:
            student_id = input("Student ID: ")
            if len(student_id):
                return student_id
            print("Student ID cannot be empty, please try again\n")

    def get_student_name():
        while True:
            name = input("Student name: ")
            if len(name):
                return name
            print("Name cannot be empty, please try again\n")

    def get_dob():
        while True:
            dob = input("Date of birth (DD/MM/YYYY): ")
            # since it wasn't allowed (yet) to check format using re module, will only check whether the string is empty
            if len(dob):
                return dob
            print("Invalid date of birth, please try again")

    return {
        "id": get_student_id(),
        "name": get_student_name(),
        "dob": get_dob()
    }


def get_number_of_courses():
    while True:
        try:
            num_course = int(input("Amount of courses: "))
            if num_course > 0:
                return num_course
            raise ValueError("Courses number cannot below zero")
        except ValueError as val:
            print(val)
        except Exception as e:
            print(f"Unexpected {e=}: {type(e)=}")
        finally:
            print()


def get_course_information(course_id):
    print(f"Course number {course_id}: ")

    def get_course_id():
        while True:
            course_id = input("Course ID: ")
            if len(course_id):
                return course_id
            print("Course ID cannot be empty, please try again\n")

    def get_course_name():
        while True:
            name = input("Course name: ")
            if len(name):
                return name
            print("Course name cannot be empty, please try again\n")

    return {
        "id": get_course_id(),
        "name": get_course_name(),
        "marks": {}
    }


def set_student_course_mark(students, courses):
    try:
        student_id = input("Student ID: ")
        if not len(student_id):
            raise ValueError("Student ID can't be empty")
        for student in students:
            if (student["id"] == student_id):
                course_id = input("Course ID: ")
                if not len(course_id):
                    raise ValueError("Course ID can't be empty")
                for course in courses:
                    if (course["id"] == course_id):
                        marks = float(input("Mark of the subject: "))
                        if marks < 0 or marks > 20:
                            raise ValueError(
                                "Subject marks can be only between 0 and 20")
                        course["marks"].update({student_id: marks})
                        return
                else:
                    raise ValueError("Course not found")
        else:
            raise ValueError("Student not found")
    except ValueError as e:
        print(f"\u001b[0;31mError: \u001b[0m{e}")


def list_courses(courses):
    print("Courses list: ")
    for i, course in enumerate(courses):
        print(f"{i + 1}. {course['name']} ({course['id']})")


def list_students(students):
    print("Student list: (format: <Name>,<ID>,<DoB>)")
    for i, student in enumerate(students):
        print(f"{i + 1}. {student['name']},{student['id']},{student['dob']}")


def get_student_course_mark(students, courses):
    try:
        student_id = input("Student ID: ")
        if not len(student_id):
            raise ValueError("Student ID can't be empty")
        for student in students:
            if (student["id"] == student_id):
                course_id = input("Course ID: ")
                if not len(course_id):
                    raise ValueError("Course ID can't be empty")
                for course in courses:
                    if (course["id"] == course_id):
                        print(f"\nStudent: {student['name']}\nCourse: {course['name']}\nMark: {course['marks'][student['id']]}")
                        return
                else:
                    raise ValueError("Course not found")
        else:
            raise ValueError("Student not found")
    except ValueError as e:
        print(f"\u001b[0;31mError: \u001b[0m{e}")


def main():
    __num_student = 0
    __num_course = 0
    __students = []
    __courses = []

    running = True

    # header
    print("Student management CLI")
    print("Author: Minotour (Tran Quoc Lan)")
    print("-------------------------------------------------------------------------------------")

    while running:
        try:
            print()
            print("Mode: \n1. Insert\n2. List\n0. Exit")
            mode = int(input("> "))
            if mode == 1:
                print("\nContext you want to enter: ")
                print("1. Number of students\n2. Students information\n3. Number of courses\n4. Courses information\n5. Score of a student in a course\n0. Back")
                ctx = int(input("> "))
                if ctx == 1:
                    __num_student = get_number_of_students()
                elif ctx == 2:
                    if not __num_student:
                        raise ValueError("num_student undefined")
                    __students = [get_student_information(i) for i in range(__num_student)]
                elif ctx == 3:
                    __num_course = get_number_of_courses()
                elif ctx == 4:
                    if not __num_course:
                        raise ValueError("num_course undefinded")
                    __courses = [get_course_information(i) for i in range(__num_course)]
                elif ctx == 5:
                    if not __num_student:
                        raise ValueError("num_student undefined")
                    if not __num_course:
                        raise ValueError("num_course undefined")
                    set_student_course_mark(__students, __courses)
                elif ctx == 0:
                    continue
                else:
                    raise ValueError("Invalid key")
            elif mode == 2:
                print("\nContext you want to list: ")
                print("1. Courses\n2. Students\n3. Mark of a student for a given course\n0. Back")
                ctx = int(input("> "))
                if ctx == 1:
                    if not __num_course:
                        raise ValueError("num_course undefined")
                    list_courses(__courses)
                elif ctx == 2:
                    if not __num_student:
                        raise ValueError("num_student undefined")
                    list_students(__students)
                elif ctx == 3:
                    if not __num_student:
                        raise ValueError("num_student undefined")
                    if not __num_course:
                        raise ValueError("num_course undefined")
                    get_student_course_mark(__students, __courses)
                elif ctx == 0:
                    continue
                else:
                    raise ValueError("Invalid key")
            elif mode == 0:
                running = False
            else:
                raise ValueError("Invalid key")
        except ValueError as e:
            print(f"\u001b[0;31mError:\u001b[0m {e}")


if __name__ == "__main__":
    main()
