import streamlit as st
from modules import functions
import os


todos = functions.get_todos()

if not os.path.exists(functions.FILEPATH):
    with open(functions.FILEPATH, "w") as file:
        pass
def add_todo():
    todo = st.session_state['new_todo'] + "\n"  # new_todo is the id of the text_input
    todos.append(todo)
    functions.write_todos(functions.FILEPATH, todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox =st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(functions.FILEPATH, todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

# Session state shows the widgets information.
# To appear in the sessions_state we need to add a key to the widget
st.session_state
