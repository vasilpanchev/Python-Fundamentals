def sort_tasks():
    tasks = []
    while True:
        command = input()
        if command == "End":
            sorted_tasks = sorted(tasks, key=lambda x: int(x.split('-')[0]))
            sorted_tasks = [task.split('-')[1] for task in sorted_tasks]
            return sorted_tasks

        tasks.append(command)


result = sort_tasks()
print(result)
