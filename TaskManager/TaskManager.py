'''
create a list - store a list of tasks


'''
import datetime as dt
import json
from prettytable import PrettyTable
tasks = [] #tasks

#add task
def add_task(title, discription, priority='low',deadline=None):
    task={

        'title':title,
        'discription':discription,
        'priority':priority,
        'deadline':deadline
    }
    tasks.append(task)


# display 
def diaplay_task():
    tk=PrettyTable(['S/No:','Title', 'Discription', 'Priority','Deadline'])
    if not tasks:
        print(" Task Not There ")
    else:
        for i,task in enumerate(tasks,start=1):
           tk.add_row([i,task['title'],task['discription'],task['priority'],task['deadline']])
        print(tk)


def delete_task( task_idx ):
    if not tasks:
        print("Task Not There ")
    elif task_idx>=len(tasks) or task_idx<0:
        print("choose correct Postion")
    else:
        remove=tasks.pop(task_idx)
        print(f'\n Task {remove["title"]} deleted \n')
        diaplay_task()

#filter by priority
def filter_by_priority(priority_level):
    pass

#filter by date
def filter_by_deadline(due_date):
    due_date=dt.strptime(due_date,'%Y-%m-%d')
   # filter_task=list(filter(lambda task:task ['deadline'] and dt.striptime(task['deadline'],'%Y-%m-%d' k==due_date),tasks))


#toggle sdtatus
def toggle_status(task_idx):
    pass

def save_data(filename):

    try:
        with open(filename, 'w') as file:
            json.dump(tasks,file)
            print('saved')
    except Exception: 
        print("not fund")

def fetch_data(filename):
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks=json.load(filename,file)
        print(tasks)
    except Exception:
        print("not found")

add_task('Give lab list','name of student','high','2024-11-13')

add_task('going the market','for buying the boxes','med','2024-11-15')

add_task('Give lab list','name of student','high','2024-11-13')

add_task('Give lab list','name of student','high','2024-11-13')

add_task('Give lab list','name of student','high','2024-11-13')

diaplay_task()

#diplaying 
