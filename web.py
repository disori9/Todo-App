import streamlit as st
import functions

st.title("My Todo App")
st.subheader("These are my todos")
todos = functions.get_file()

for todo in todos:
     st.checkbox(todo)


st.text_input(label="", placeholder="Enter a todo:")\

