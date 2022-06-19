from todo_app.models import ToDoList


def run():
    # Fetch all questions
    questions = ToDoList.objects.all()
    # Delete questions
    questions.delete()
