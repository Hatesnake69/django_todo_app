from todo_app.models import ToDoItem, ToDoList
import json


question2 = ToDoItem.objects.filter(id=100, todo_list_id=100)[0]
history_dict = dict()
for history in question2.history.all():
    history_dict[history.history_id] = {
        'history_id': history.id,
        'title': history.title,
        'description': history.description,
        'history_date': history.history_date.strftime("%m/%d/%Y, %H:%M:%S")
    }

print(json.dumps(
    {"id": f"{question2.id}", "created": question2.created_date.strftime("%m/%d/%Y, %H:%M:%S"), "history_detail": history_dict},
    indent=7
))
