import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(key="todo")
add_button = sg.Button("Add")


window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Verdana', 12))

# event returns button label (because clicking button is an event,
# values return a dictionary type consisting of what was inputted in the input box
while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = functions.get_file()
            todos.append(values['todo'] + '\n')
            functions.write_file(todos)
window.close()

