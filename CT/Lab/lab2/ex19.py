class Task:
    def __init__(self, description, priority):
        self.description, self.priority, self.status = description, priority, "Pending"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_completed(self, description):
        for t in self.tasks:
            if t.description == description:
                t.status = "Done"
                print(f"{t.description} done")
                return
        print("Cannot do task.")

    def change_priority(self, description, new_priority):
        for t in self.tasks:
            if t.description == description:
                t.priority = new_priority
                print(f"Change priority: {t.description} → {new_priority}")
                return
        print("Cannot do task.")

    def list_tasks(self):
        print("\n Tasks list:")
        for t in sorted(self.tasks, key=lambda x: x.priority):
            print(f"- {t.description} | Priority: {t.priority} | Status: {t.status}")

tm = TaskManager()
tm.add_task(Task("Learn Python", 2))
tm.add_task(Task("House chores", 3))
tm.add_task(Task("Homework", 1))

tm.list_tasks()
tm.mark_completed("Learn Python")
tm.change_priority("House chores", 1)
tm.list_tasks()
