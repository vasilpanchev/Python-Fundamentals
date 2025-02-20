def add_lesson(lesson_title: str, lessons: list):
    if lesson_title not in lessons:
        lessons.append(lesson_title)


def insert_lesson(lesson_title: str, index: int, lessons: list):
    if lesson_title not in lessons:
        lessons.insert(index, lesson_title)


def remove_lesson(lesson_title: str, lessons: list):
    exercise = f"{lesson_title}-Exercise"

    if lesson_title in lessons:
        lessons.remove(lesson_title)

    if exercise in lessons:
        lessons.remove(exercise)


def swap_lessons(lesson_title_1: str, lesson_title_2: str, lessons: list):
    # index_1 = -1
    # index_2 = -1
    exercise_1 = f"{lesson_title_1}-Exercise"
    exercise_2 = f"{lesson_title_2}-Exercise"

    if lesson_title_1 in lessons and lesson_title_2 in lessons:
        #  for i in range(len(lessons)):
        #     if lessons[i] == lesson_title_1:
        #         index_1 = i
        #         if index_2 != -1:
        #             break
        #     elif lessons[i] == lesson_title_2:
        #         index_2 = i
        #         if index_1 != -1:
        #             break

        index_1 = lessons.index(lesson_title_1)
        index_2 = lessons.index(lesson_title_2)
        lessons[index_1], lessons[index_2] = lessons[index_2], lessons[index_1]

        if exercise_1 in lessons:
            lessons.remove(exercise_1)
            lessons.insert(index_2 + 1, exercise_1)

        if exercise_2 in lessons:
            lessons.remove(exercise_2)
            lessons.insert(index_1 + 1, exercise_2)


def add_exercise(lesson_title: str, lessons: list):
    exercise = f"{lesson_title}-Exercise"

    if lesson_title not in lessons:
        add_lesson(lesson_title, lessons)

    if exercise not in lessons:
        index = lessons.index(lesson_title)
        lessons.insert(index + 1, exercise)


course_program = input().split(', ')

while True:
    command = input().split(":")

    if command[0] == "course start":
        for i in range(len(course_program)):
            print(f"{i + 1}.{course_program[i]}")
        break

    elif command[0] == "Add":
        title = command[1]
        add_lesson(title, course_program)

    elif command[0] == "Insert":
        title = command[1]
        index = int(command[2])
        insert_lesson(title, index, course_program)

    elif command[0] == "Remove":
        title = command[1]
        remove_lesson(title, course_program)

    elif command[0] == "Swap":
        title_1 = command[1]
        title_2 = command[2]
        swap_lessons(title_1, title_2, course_program)

    elif command[0] == "Exercise":
        title_1 = command[1]
        add_exercise(title_1, course_program)