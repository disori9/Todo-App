import streamlit as st
import functions

def add_todo():
     input_todo = st.session_state['new_todo'] + '\n'
     print(input_todo)
     todos_local = functions.get_file()
     todos_local.append(input_todo)
     functions.write_file(todos_local)

st.title("My Todo App")
st.subheader("These are my todos")
todos = functions.get_file()

for todo in todos:
     st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo:",
              key="new_todo", on_change=add_todo)


