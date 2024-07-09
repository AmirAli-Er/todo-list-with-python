import tkinter
import todo
import json


window = tkinter.Tk()
window.title('todo list')
window.resizable(width=False, height=False)


frame1 = tkinter.LabelFrame(window, text='Todos', fg='white', width=600, height=250, bg='#424242')
frame1.grid(row=0, column=0, sticky='nsew')


# creating todos
with open('todos.json', 'r') as json_file:
    todos = json.load(json_file)
    for tod in todos['todos']:
        todo.Todo(tod['title'], tod['is_done'], tod['description'], frame1)


frame2 = tkinter.LabelFrame(window, text='Add your todo', width=600, height=150, bg='gray', padx=10, pady=10)
frame2.grid(row=1, column=0, sticky='nsew')


def add_new_todo():
    if title_input.get():
        todo.Todo(title_input.get(), False, description_input.get(), frame1)
    else:
        pass


def save_function():
    todo.Todo.save_todos()
    window.destroy()


title_label = tkinter.Label(frame2, text='Todo title : ', bg='gray')
description_label = tkinter.Label(frame2, text='Todo description : ', bg='gray')
title_input = tkinter.Entry(frame2, width=25)
description_input = tkinter.Entry(frame2, width=25)
todo_submit = tkinter.Button(frame2, text='submit', padx=12, command=add_new_todo)
title_label.grid(row=0, column=0)
title_input.grid(row=0, column=1)
description_label.grid(row=1, column=0)
description_input.grid(row=1, column=1)
todo_submit.grid(row=2, column=4, padx=12, pady=12)
window.protocol("WM_DELETE_WINDOW", save_function)




window.mainloop()
