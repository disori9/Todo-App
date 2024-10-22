import functions
import PySimpleGUI as sg

from functions import write_file

label = sg.Text("Type in a todo")
input_box = sg.InputText(key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_file(), key="todos",
                   enable_events=True, size=(44,10))
edit_button = sg.Button("Edit")

layout = [[label],
          [input_box, add_button],
          [list_box, edit_button]]

window = sg.Window('My To-Do App', layout, font=('Verdana', 12))

# event returns button label (because clicking button is an event,
# values return a dictionary type consisting of what was inputted in the input box
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_file(todos)

        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'

            todos = functions.get_file()
            replacetodo_index = todos.index(todo_to_edit)
            todos[replacetodo_index] = new_todo
            write_file(todos)

        case sg.WINDOW_CLOSED:
            break
window.close()

