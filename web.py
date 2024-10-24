import streamlit as st
import functions

todos = functions.get_file()
def add_todo():
     input_todo = st.session_state['new_todo'] + '\n'
     todos.append(input_todo)
     functions.write_file(todos)

st.title("My Todo App")
st.subheader("These are my todos")

# sadly, i do not know streamlit that well yet so i am unable to implement
# showing the completed_todo functions
for index, todo in enumerate(todos):
     todo_checkbox = st.checkbox(todo, key=todo) # every key should be unique, so we could identify what is being clicked.
     if todo_checkbox is True: # when a checkbox is clicked, it returns to true
          todos.pop(index) # we implement the enumerate function to know the current iteration of to do that is clicked, so we can remove it
          # although we could've also done this: todos.remove(todo)
          functions.write_file(todos)
          # and then we rewrite todos existing file
          del st.session_state[todo]
          # we need to delete the unique session_state of the removed todo so we can clean the dictionary
          st.experimental_rerun()
          # seems like this is needed for checkboxes.

# on_change basically says na if something is entered in the text_input
# it would run the function add_todo(), though i do not know why it does not have any parameters to be allowed

st.text_input(label="", placeholder="Enter a todo:",
              key="new_todo", on_change=add_todo)

