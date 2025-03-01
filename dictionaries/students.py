class Students:
    def __init__(self):
        self.students = {}

    def add_student(self, name, ID, course):
        course_id = {ID: course}
        self.students[name] = course_id

    def students_in_course(self, course_to_find) -> list:
        result = []
        for (name, course) in self.students.items():
            (ID, course) = course.popitem()
            if course == course_to_find:
                result.append(f"{name} - {ID}")

        return result


def main():
    students = Students()
    command = input()
    while ":" in command:
        name, ID, course = command.split(":")
        students.add_student(name, ID, course)
        command = input()
    course_to_find = command
    course_to_find = ' '.join(course_to_find.split("_"))
    print('\n'.join(students.students_in_course(course_to_find)))


if __name__ == "__main__":
    main()
