import datetime
import tkinter
import json


class Todo:
    todos_dict = {
        'todos': []
    }
    @staticmethod
    def cross_out(texts):

        return "\u0336".join(texts.replace(" ", "\u00a0")) + "\u0336"

    def visible_command(self):
        if self.checkbutton_value.get() == 0:
            self.checkbutton_done.pack_forget()
            self.checkbutton_undone.pack()
            self.is_done = False
            for i in Todo.todos_dict['todos']:
                if i['id'] == self.id:
                    Todo.todos_dict['todos'][Todo.todos_dict['todos'].index(i)]['is_done'] = False

        else:
            self.checkbutton_undone.pack_forget()
            self.checkbutton_done.pack()
            self.is_done = True
            for i in Todo.todos_dict['todos']:
                if i['id'] == self.id:
                    Todo.todos_dict['todos'][Todo.todos_dict['todos'].index(i)]['is_done'] = True

    def __init__(self, title, is_done, description, window):
        self.title = title
        self.id = len(Todo.todos_dict['todos'])
        self.is_done = is_done
        self.date = f'{datetime.datetime.now().hour} {datetime.datetime.now().day}'
        self.description = description
        self.window = window
        self.frame = tkinter.LabelFrame(self.window, text=self.title, bg='#424242', fg= 'white', width=200)
        self.des_label = tkinter.Label(self.frame, text=self.description, fg='white')
        self.checkbutton_value = tkinter.IntVar()  # value of check button(0 or 1)
        self.checkbutton_undone = tkinter.Checkbutton(self.frame, text=self.description,
                                               variable=self.checkbutton_value,
                                               onvalue=1,
                                               offvalue=0, bg='#424242', fg='blue', command=self.visible_command)
        self.checkbutton_undone.pack()
        self.checkbutton_done = tkinter.Checkbutton(self.frame, text=Todo.cross_out(self.description),
                                               variable=self.checkbutton_value,
                                               onvalue=1,
                                               offvalue=0, bg='#424242', fg='blue', command=self.visible_command)
        self.frame.grid(row=len(Todo.todos_dict['todos']), column=1, sticky='NW')

        Todo.todos_dict['todos'].append({'title': self.title, 'description': self.description, 'is_done': self.is_done, 'date': self.date, 'id': self.id})

    @classmethod
    def save_todos(cls):
        ls = []
        for i in Todo.todos_dict['todos']:
            if not i['is_done']:
                ls.append(i)
        with open('todos.json', 'w+') as json_file:
            json.dump({'todos': ls}, json_file)