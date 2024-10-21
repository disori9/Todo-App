import functions
import time

print(f"It is {time.strftime('Day %d of %B, %Y')}.")
while True:
    user_action = input("Type add (text), show, edit (todo number), complete (todo number), show completed or end: ")

    if user_action.lower().strip().startswith('add') or user_action.lower().strip().startswith('new'):
        todo = user_action[4:] + "\n"
        # [4:] means to just get the string after 'add '
#basically, ang ginagawa natin is inoopen natin yung todos.txt with mode r which is read.
#after nun, gagamitin natin ang method na .readlines() ng file object (file variable, sorry for confusion.)
#readlines ay nagbabalik ng list, na nagcocontain ng iba't ibang linya sa binasang file.
#isasave natin yung list na yun sa variable na todos, at magaappend doon.
        todos = functions.get_file()
#after iappend, ioopen uli natin ang todos.txt gamit ang function na open() na w ang mode which is write
#and then gagamitin natin ang .writelines() method ng file (sa loob ng parameter ay isang list or string or kahit ano
#para mailagay natin yung list ng todos at ng mga text na todos last instance sa todos.txt (para hindi maclear yung dating nakalagay.)
        todos.append(todo)

        functions.write_file(todos)

    elif user_action.lower().strip() == 'show':
        # todos = get_file('todos.txt')
        # new_todos = [item.strip() for item in todos]
        # an alternative in the method below, removing the \n in the list.
        #for index, item in enumerate(todos):
        #    print(f"{index + 1}) {item.strip()}")
        functions.show_file()

    elif user_action.lower().strip() == 'show completed':
        functions.show_file('completed_todos.txt')

    elif 'end' == user_action.lower().strip():
        break

    elif user_action.lower().strip().startswith('edit'):
        try:
            todos = functions.get_file()

            #edit_number = int(input("What number in the todo list do you wish to replace? "))
            edit_number = int(user_action[5:])
            insert_new_item = input("What do you wish to replace it with? ") + "\n"
            todos[edit_number - 1] = insert_new_item

            functions.write_file(todos)

        except ValueError:
            print('\nYou need to input the number of the to do list you want to edit.')
            print('Here are your current list of to dos: ')

            functions.show_file()
            print('')
            continue

        except IndexError:
            print('\nYou need to input a VALID number of the to do list you want to edit.')
            print('Here are your current list of to dos: ')

            functions.show_file()
            print('')
            continue

    elif user_action.lower().strip().startswith('complete'):
        try:
            #completed_todo_index = int(input("What number of todo was completed? "))
            completed_todo_index = int(user_action[9:])
            #inopen muna natin yung file, at ginawa yung list na todos. reason being, kailangan natin makuwa yung lahat ng todos.
            #pag di natin ginawa to, pag di natin ginamit yung add na command, walang magagawang todos na variable at hindi natin maaccess yung kailangan natin icomplete
            #resulting into an error.
            todos = functions.get_file()

            #siyempre ioopen rin natin ang completed_todos.txt at ilalagay ang nandoon sa isang variable, para malagay natin lahat ng completed_todos kahit sa dating instances.
            completed_todos = functions.get_file('completed_todos.txt')

            #appending yung piniling number of todo na nacomplete ng user..
            completed_todo = todos.pop(completed_todo_index - 1)
            completed_todos.append(completed_todo)

            #iopen muna natin todos, with write at ioverwrite yung file with bagong (naremovean na variable) na variables.
            functions.write_file(todos)

            #iopen completed_todos.txt, at iwrite ang list ng bagong completed_todos
            functions.write_file(completed_todos, 'completed_todos.txt')

            print(f"Good job! you completed {completed_todo.strip()}!")

        except ValueError:
            print('\nYou need to input the number of the to do list you want to complete.')
            print('Here are your current list of to dos: ')

            functions.show_file()
            continue

        except IndexError:
            print('\nYou need to input a VALID number of the to do list you want to complete.')
            print('Here are your current list of to dos: ')

            functions.show_file()
            continue

    else:
        print('Unknown command!')


print("Thank you!")

