from todo_app.models import ToDoList, ToDoItem


def run():
        question1 = ToDoList(title='list1', pk=100)
        question1.save()
        question2 = ToDoItem(title='task1', description='task', todo_list=question1, pk=100)
        question2.save()
    # Delete questions


