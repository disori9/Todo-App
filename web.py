import streamlit as st
import functions

todos = functions.get_file()
def add_todo():
     input_todo = st.session_state['new_todo'] + '\n'
     todos.append(input_todo)
     functions.write_file(todos)


st.title("My Todo App")
st.subheader("These are my todos")

for index, todo in enumerate(todos):
     todo_checkbox = st.checkbox(todo, key=todo)
     if todo_checkbox is True:
          todos.pop(index)
          functions.write_file(todos)
          del st.session_state[todo]
          st.experimental_rerun()

st.text_input(label="", placeholder="Enter a todo:",
              key="new_todo", on_change=add_todo)

st.session_state