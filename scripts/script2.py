from todo_app.models import ToDoList, ToDoItem
import random
import time


def run():
    question2 = ToDoItem.objects.filter(id=100, todo_list_id=100)[0]
    list_of_titles = ['pupa', 'lupa', 'dupa', 'zupa', 'mupa']
    list_of_descriptions = ['asada', 'vvvvasvaf', 'ppppaaeq', 'llloaass']
    for i in range(10):
        question2.title = random.choice(list_of_titles)
        question2.description = random.choice(list_of_descriptions)
        question2.save()
        time.sleep(1)