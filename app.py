import streamlit as st
from task_manager import TaskManager

# Streamlit App Layout
st.title("Simple To-Do List 📝")
st.markdown("---")  # Horizontal line for separation

# Initialize TaskManager
task_manager = TaskManager()

# Task Type Selection
task_type = st.selectbox("Choose Task Type", ["Personal", "Work"])

# Initialize session state for form fields
if 'title' not in st.session_state:
    st.session_state['title'] = ""
if 'description' not in st.session_state:
    st.session_state['description'] = ""

# Task Form
with st.form("task_form"):
    col1, col2 = st.columns(2)  # Create two columns for better layout
    with col1:
        title = st.text_input("Task Title", value=st.session_state['title'])
    with col2:
        due_date = st.date_input("Due Date")

    description = st.text_area("Task Description", value=st.session_state['description'])
    submitted = st.form_submit_button("Add Task")

    if submitted:
        if not title or not description:
            st.error("Please fill in both Title and Description!")
        else:
            task_manager.add_task("personal" if task_type == "Personal" else "work", title, description, due_date)
            st.success(f"{task_type} Task added successfully! 🥳")

            # Clear input fields in session state
            st.session_state['title'] = ""
            st.session_state['description'] = ""

            # Instead of rerun, we can just refresh the displayed tasks


# Fetch and display tasks
st.subheader("Your Tasks")
all_tasks = task_manager.get_all_tasks()

if all_tasks:
    for task in all_tasks:
        # Display task with checkboxes for completion
        completed = st.checkbox(f"**{task['title']}** 🗑️", value=False, key=task["_id"])  # Use task ID as the key
        st.write(f"**Description**: {task['description']}")
        st.write(f"**Due Date**: {task['due_date']}")

        # Delete button with an icon
        if st.button(f"Delete {task['title']} 🗑️", key=f"delete_{task['_id']}"):
            task_manager.delete_task(task["_id"])
            st.success(f"{task['title']} deleted.")
            # Fetch the updated tasks after deletion
            all_tasks = task_manager.get_all_tasks()
else:
    st.write("No tasks available. Please add some!")
