

class Todo:
    def __init__(self,title,priority):
        self.title = title
        self.priority = priority
        self.task_id = len(tasks)+1

tasks = []

while True:
    title = input("Enter task title or q to quit: ")
    if(title == "q"):
        break 
    priority = input("Enter priority: ")

    task = Task(title,priority)

    tasks.append(task)

    print(len(tasks))


for task in tasks:
    print(task.task_id)
    print(task.title)
    print(task.priority)


print("Thanks for using list app")
