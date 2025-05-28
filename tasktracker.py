import json
task_id = 0


class Task:
    #add date to task object
    #refactor status with some method that updates status
    def __init__(self, task, description, status,**kwargs):
        self.task = task
        global task_id
        task_id += 1
        self.id = task_id
        self.description = description
        statuss = dict()
        statuss[1] = 'Todo'
        statuss[2] = 'In progress'
        statuss[3] = 'Done'
        try:
            self.status = statuss[status]
        except KeyError:
            print('You can only choose from 1-3')

    def change_task_id(self,task_id):
        self.id = task_id

    def search_task(self,word):
        return word in self.description or word in self.task

    def change_to_dict(self):
        stored_data = dict()
        stored_data['task'] = self.task
        stored_data['task_id'] = self.id
        stored_data['description'] = self.description
        stored_data['status'] = self.status
        return stored_data

class TaskTracker:
    def __init__(self):
        self.tasks = []
        self.tasks_todo = []
        self.tasks_progress = []
        self.tasks_done = []

    def add_new_task(self):
        task = input("enter your task")
        description = input('enter your task description')
        status = int(input('enter your status \n1.todo\n2.in-progress\n3.done'))
        self.tasks.append(Task(task,description,status))
        

    def search__task(self,id_task):
        for task in self.tasks:
            if id_task == task.id :
                return task
            else:
                return False

    def update_task(self,id_task,taskk=''):
        task = self.search__task(id_task)
        task.task = taskk

    def delete_task(self,id_task):
        task = self.search__task(id_task)
        extracted_task = task
        self.tasks.remove(extracted_task)

    def display_tasks(self):
        print('Tasks')
        for task in self.tasks:
            print(f"\n id : {task.id}\n name : {task.task}\n description : {task.description}\n status : {task.status}")
    #refactor this code where it shows all the other tasks list or make another method
    def priority_task(self,id_task):
        id_task -= 1
        popped_task = self.tasks.pop(id_task)
        self.tasks.insert(0,popped_task)

    def save_all(self):
        data = self.tasks
        filename = 'data.json'
        with open(filename, 'w') as file:
            json.dump([d.change_to_dict() for d in data],file)


    # save all tasks in .json file

    def load_all(self):
        filename = 'data.json'
        with open(filename) as f:
            extracted = json.load(f)
        for x in extracted:
            task = x['task']
            description = x['description']
            if x['status'] == 'Todo':
                status = 1
            elif x['status'] == 'In progress':
                status = 2
            elif x['status'] == 'Done':
                status = 3
            task_01 = Task(task,description,status)
            task_01.change_task_id(x['task_id'])
            self.tasks.append(task_01)


    # load all tasks in TaskTracker object
    # manipulate data
    # see if it works

    def listing_up(self):
        for task in self.tasks:
            if task.status == 'Todo':
                copied_task = task.copy()
                self.tasks_todo.append(copied_task)
            elif task.status == 'In progress':
                copied_task = task.copy()
                self.tasks_progress.append(copied_task)
            elif task.status == 'Done':
                copied_task = task.copy
                self.tasks_done.append(copied_task)




class TaskTrackerRun(TaskTracker):
    def __init__(self):
        super().__init__()
        print('This is the menu for Task Tracker , press number as per your requirement:')
        active = True
        while active:
            returned_num = self.inter_face()
            if returned_num == 'q':
                active = False
            else:
                self.backend_interface(int(returned_num))

    def inter_face(self):
        list_1 = ['add task','display tasks','save all','update task','search task','delete task','set priority for task',]
        menu = dict(zip(range(1,8),list_1)) #this is a dict comprehension , basically creating a dict to number down list_1
        for key,val in menu.items():
            print(f'{key} : {val}')
        print('press q when you are done')
        num_ber = input('enter your number here')
        return num_ber

    def backend_interface(self,number_r):
        if number_r not in range(1,8):
            return False

        print(f'number recieved and its type {number_r} , {type(number_r)}')

        if number_r == 1:
            super().add_new_task()
        if number_r == 2:
            super().display_tasks()



        #CODE IS WORKING FOR NOW BUT REFACTOR IT AT A LATER DATE
if __name__ == '__main__':
    a = TaskTrackerRun()




























