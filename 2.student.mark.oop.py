COLOR_RED = "\u001b[0;31m"
COLOR_RESET = "\u001b[0m"


class Student():
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__dob = None

    # Student id
    def get_id(self):
        return self.__id

    def set_id(self, _id: str):
        if not len(_id):
            raise ValueError("id can't be empty")
        self.__id = _id

    # Name
    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if not len(name):
            raise ValueError("name can't be empty")
        self.__name = name

    # Date of birth
    def get_dob(self):
        return self.__dob

    def set_dob(self, date_list: str):
        date_list = list(map(int, date_list.split('/', 2)))

        if date_list[2] <= 0 or date_list[2] > 9999:
            raise ValueError("Invalid year")
        if date_list[1] <= 0 or date_list[1] > 12:
            raise ValueError("Invalid month")

        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (date_list[0] <= 0 or
            date_list[0] > days_in_month[date_list[1] - 1]
            + (date_list[2] % 400 == 0 or
               (date_list[2] % 4 == 0 and date_list[2] % 100))):
            raise ValueError("Invalid day")

        self.__dob = f"{date_list[0]:02d}/"\
                     f"{date_list[1]:02d}/"\
                     f"{date_list[2]:04d}"


class Course():
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__marks = {}  # format {Student(): float}

    # Student id
    def get_id(self):
        return self.__id

    def set_id(self, _id: str):
        if not len(_id):
            raise ValueError("id can't be empty")
        self.__id = _id

    # Name
    def get_name(self):
        return self.__name

    def set_name(self, name: str):
        if not len(name):
            raise ValueError("name can't be empty")
        self.__name = name

    # Mark
    def get_mark(self, student: Student):
        return (self.__marks[student]
                if student in self.__marks.keys()
                else None)

    def set_mark(self, student: Student, mark: float):
        if mark < 0 or mark > 20:
            raise ValueError("Student mark can be only between 0 and 20")
        self.__marks.update({student: mark})


class School(Student, Course):
    def __init__(self):
        super().__init__()
        self.__num_students = 0
        self.__students = []

        self.__num_courses = 0
        self.__courses = []

    # Num students
    def get_num_students(self):
        if self.__num_students <= 0:
            raise ValueError("Students list is empty")
        return self.__num_students

    def set_num_students(self, num_students):
        if num_students <= 0:
            raise ValueError(f"Invalid number of students ({num_students})")
        self.__num_students = num_students

    # Num courses
    def get_num_courses(self):
        if self.__num_courses <= 0:
            raise ValueError("Courses list is empty")
        return self.__num_courses

    def set_num_courses(self, num_courses):
        if num_courses <= 0:
            raise ValueError(f"Invalid number of courses ({num_courses})")
        self.__num_courses = num_courses

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def __append_student(self, student):
        self.__students.append(student)

    def __append_course(self, course):
        self.__courses.append(course)

    def input_student(self):
        student = Student()

        student.set_id(input("Student ID: "))
        student.set_name(input("Student name: "))
        student.set_dob(input("Student date of birth (DD/MM/YYYY): "))

        self.__append_student(student)

    def input_course(self):
        course = Course()

        course.set_id(input("Course ID: "))
        course.set_name(input("Course name: "))

        self.__append_course(course)

    def input_students(self):
        if self.__num_students <= 0:
            raise ValueError("Students amount can't be 0")
        self.__students.clear()
        for i in range(self.__num_students):
            print(f"\nInfo of student {i + 1}: ")
            self.input_student()

    def input_courses(self):
        if self.__num_courses <= 0:
            raise ValueError("Courses amount can't be 0")
        self.__courses.clear()
        for i in range(self.__num_courses):
            print(f"\nInfo of course {i + 1}: ")
            self.input_course()

    def list_students(self):
        if self.__students is None:
            raise Exception("Student list is empty")

        print("\nStudent list: ")
        for i, student in enumerate(self.__students):
            print(
                    f"{i + 1}. {student.get_name()} ({student.get_id()}) "
                    f"- {student.get_dob()}"
            )

    def list_courses(self):
        if self.__courses is None:
            raise Exception("Course list is empty")

        print("\nCourse list: ")
        for i, course in enumerate(self.__courses):
            print(f"{i + 1}. {course.get_id()} - {course.get_name()}")

    def get_student(self, student_id):
        for student in self.get_students():
            if student.get_id() == student_id:
                return student
        return None

    def get_course(self, course_id):
        for course in self.get_courses():
            if course.get_id() == course_id:
                return course
        return None



def main():
    school = School()
    __running = True

    # Prompt function and return selection from user
    def prompt_command(prompts):
        for p in prompts:
            print(p)
        return int(input("> "))

    # Header
    print("Student marks management (OOP edition)")
    print("Author: Minotour (Tran Quoc Lan)")
    print("-----------------------------------------")

    # Insert mode
    def _insert_mode():
        ctx_mode = prompt_command([
            "\nContext to insert: ",
            "1. Number of students",
            "2. List of students",
            "3. Number of courses",
            "4. List of courses",
            "5. Mark of a student in a course"
            ])
        if ctx_mode == 1:
            school.set_num_students(int(input("Number of students: ")))
        elif ctx_mode == 2:
            school.input_students()
        elif ctx_mode == 3:
            school.set_num_courses(int(input("Number of courses: ")))
        elif ctx_mode == 4:
            school.input_courses()
        elif ctx_mode == 5:
            course = school.get_course(input("Course id: "))
            if course is None:
                raise ValueError("No course found")
            student = school.get_student(input("Student id: "))
            if student is None:
                raise ValueError("No student found")
            course.set_mark(student,
                            float(input("Mark of the student: ")))
        else:
            raise ValueError("Invalid selection")

    # List mode
    def _list_mode():
        ctx_mode = prompt_command([
            "\nContext to list: ",
            "1. List of students",
            "2. List of courses",
            "3. Mark of a student in a course"
            ])
        if ctx_mode == 1:
            school.list_students()
        elif ctx_mode == 2:
            school.list_courses()
        elif ctx_mode == 3:
            course = school.get_course(input("Course id: "))
            if course is None:
                raise ValueError("No course found")
            student = school.get_student(input("Student id: "))
            if student is None:
                raise ValueError("No student found")
            mark = course.get_mark(student)
            if mark is None:
                raise ValueError("Student have no mark in this course")
            print(
                f"\nName: {student.get_name()}\n"
                f"Course: {course.get_name()}\n"
                f"Mark: {mark}"
            )

    def _main_mode():
        main_prompt = prompt_command([
            "\nMode: ",
            "1. Insert",
            "2. List",
            "0. Exit"
            ])

        if main_prompt == 1:
            _insert_mode()
        elif main_prompt == 2:
            _list_mode()
        elif main_prompt == 0:
            print("Exiting...")
            exit(0)
        else:
            raise ValueError("Invalid selection")

    while __running:
        try:
            _main_mode()
        except Exception as e:
            if isinstance(e, ValueError):
                print(f"{COLOR_RED}{type(e).__name__}: {COLOR_RESET}{e}")
            else:
                print(
                        f"Unknown error {COLOR_RED}{type(e).__name__}: "
                        f"{COLOR_RESET}{e}"
                )


if __name__ == "__main__":
    main()
