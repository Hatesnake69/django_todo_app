from todo_app.models import ToDoList, ToDoItem
import random
import json
import time


def run():
    for i in range(10):
        question1 = ToDoList(title=f'list{i}') #script1
        question1.save() #script1
        question2 = ToDoItem(title=f'task1', description='task1', todo_list=question1) #script1
        question2.save() #script1

        question3 = ToDoItem.objects.filter( #script2
            todo_list_id=ToDoList.objects.filter(title=f'list{i}')[0].id #script2
        )[0] #script2
        list_of_titles = ['pupa', 'lupa', 'dupa', 'zupa', 'mupa'] #script2
        list_of_descriptions = ['asada', 'vvvvasvaf', 'ppppaaeq', 'llloaass'] #script2
        for j in range(10): #script2
            question3.title = random.choice(list_of_titles) #script2
            question3.description = random.choice(list_of_descriptions) #script2
            question3.save() #script2
            time.sleep(1) #script2

        question4 = ToDoItem.objects.filter( #script3
            todo_list_id=ToDoList.objects.filter(title=f'list{i}')[0].id #script3
        )[0] #script3
        history_dict = dict() #script3
        for history in question4.history.all(): #script3
            history_dict[history.history_id] = { #script3
                'history_id': history.id, #script3
                'title': history.title, #script3
                'description': history.description, #script3
                'history_date': history.history_date.strftime("%m/%d/%Y, %H:%M:%S") #script3
            } #script3

        print(json.dumps( #script3
            {
                "title": f"{question4.title}",  # script3
                "id": f"{question4.id}", #script3
                "created": question4.created_date.strftime("%m/%d/%Y, %H:%M:%S"), #script3
                "history_detail": history_dict #script3
            }, #script3
            indent=7 #script3
        )) #script3
