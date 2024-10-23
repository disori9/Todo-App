import time
import functions
import PySimpleGUI as sg

sg.theme('DarkPurple1')
clock_text = sg.Text(key='clock', font=('Verdana', 9))
label = sg.Text("Type in a todo")
input_box = sg.InputText(key="todo")
add_button = sg.Button("Add", font=('Verdana', 10))
list_box = sg.Listbox(values=functions.get_file(), key="todos",
                   enable_events=True, size=(44,10))
edit_button = sg.Button("Edit", font=('Verdana', 10))
complete_button = sg.Button("Complete", font=('Verdana', 10))
exit_button = sg.Button("Exit", font=('Verdana', 10))
show_todos_button = sg.Button("Show To Dos", font=('Verdana', 10))
show_complete_button = sg.Button("Show Completed To Dos", font=('Verdana', 10))

layout = [[clock_text],
          [label],
          [input_box, ],
          [list_box, [add_button, edit_button, complete_button, exit_button]],
          [show_todos_button, show_complete_button]]

window = sg.Window('My To-Do App', layout, font=('Verdana', 12))

# event returns button label (because clicking button is an event,
# values return a dictionary type consisting of what was inputted in the input box
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%B %d, %Y | It is %A | %I:%M %p'))

    match event:
        case "Add":
            todos = functions.get_file()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_file(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + '\n'

                todos = functions.get_file()
                replacetodo_index = todos.index(todo_to_edit)
                todos[replacetodo_index] = new_todo
                functions.write_file(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('Please select a todo to edit!', button_justification='center', font=('Verdana', 11))
                continue

        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_file()
                completed_todo = todos.pop(todos.index(todo_to_complete))
                completed_todos = functions.get_file('completed_todos.txt')
                completed_todos.append(completed_todo)
                functions.write_file(todos)
                functions.write_file(completed_todos, 'completed_todos.txt')
                window['todos'].update(values=functions.get_file())
                window['todo'].update(value="")
                sg.popup(f'You have successfully completed {todo_to_complete.strip()}!', button_justification='center', font=('Verdana', 11))
            except IndexError:
                sg.popup('Please select a todo to complete!', button_justification='center', font=('Verdana', 11))
                continue

        case "Exit":
            break

        case "todos":
            window['todo'].update(values['todos'][0].strip())

        case "Show To Dos":
            window['todos'].update(values=functions.get_file())

        case "Show Completed To Dos":
            window['todos'].update(values=functions.get_file('completed_todos.txt'))

        case sg.WINDOW_CLOSED:
            break
window.close()

