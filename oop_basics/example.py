class Person:
    def __init__(self, first_name, last_name, age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


people = []
command = input()
while command != "End":
    first_name, last_name, age = command.split()
    current_person = Person(first_name, last_name, int(age))
    people.append(current_person)
    command = input()
for person in people:
    print(f"{person.first_name} {person.last_name} is {person.age} years old.")
