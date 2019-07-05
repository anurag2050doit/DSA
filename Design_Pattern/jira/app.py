class User:
    _tasks = set()
    name = None

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def add_task(self, task):
        self._tasks.add(task)

    def get_all_task(self):
        for task in self._tasks:
            print(task)

    def remove_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)
            return self._tasks
        else:
            return 'This is not assigned to %s user' % self.name


class Task:
    task_type = None
    name = None
    desc = None
    status = None

    def __init__(self, task_type, name, status, desc=None):
        self.task_type = task_type
        self.name = name
        self.status = status
        self.desc = desc

    def __str__(self):
        return self.name

    def change_status(self, status):
        self.status = status


class Sprint:
    _tasks = set()
    name = None

    def __init__(self, name):
        self.name = name

    def add_task(self, task):
        self._tasks.add(task)

    def get_all_task(self):
        for task in self._tasks:
            print(task)

    def remove_task(self, task):
        if task in self._tasks:
            self._tasks.remove(task)
            print('%s task is removed from %s sprint' % (str(task), self.name))
            return self._tasks
        else:
            return 'This task is not added to %s this sprint' % self.name


if __name__ == '__main__':
    print('Creating User')
    user1 = User('Anurag')
    user2 = User('Aman')
    print('Creating a task')
    task1 = Task('Story', 'Easy Task', 'Incomplete')
    task2 = Task('Feature', 'Easy Task 1', 'Incomplete')
    task3 = Task('Bugs', 'Easy Task 2', 'Incomplete')
    print('Creating a sprint')
    sprint1 = Sprint('Week1')
    print('Assigning tasks to User1')
    user1.add_task(task1)
    user1.add_task(task2)
    print('Assigning tasks to User2')
    user2.add_task(task2)
    user2.add_task(task3)
    print('Adding task to sprint')
    sprint1.add_task(task1)
    sprint1.add_task(task2)
    sprint1.add_task(task3)
    print('Get all the task of User1')
    user1.get_all_task()
    print('Get all the task of User2')
    user2.get_all_task()
    sprint1.remove_task(task2)
