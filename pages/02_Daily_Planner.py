import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import openai
import datetime

legalease = Image.open("assets/LegalEase.jpg")

st.set_page_config(page_title="LegalEase - Daily Planner", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
#st.sidebar.title("LegalEase")
st.sidebar.image(legalease)

# Use the following line to include your style.css file
#st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

st.header("LegalEase")
st.subheader("Daily Planner")

st.write("*Unable to take appropriate breaks at work due to your hectic schedule? Daily Planner got you covered! Just input your tasks for the day and the approximate time required in the fields below!*")

openai.api_key = st.secrets['openai_key']

can_confirm = [False, False] 

story = "Man decides to start work at "
# User's working hours
start_time = st.time_input("Select when your working day starts", value=datetime.time())
end_time = st.time_input("Select when your working day ends", value=datetime.time())
if (start_time >= end_time):
    st.write("End time has to be after the start time")
    can_confirm[0] = False
else:
    can_confirm[0] = True
    story += start_time.strftime("%H:%M:%S")[:-3]
    story += " and decides to end work at "
    story += end_time.strftime("%H:%M:%S")[:-3]
    story += "."
    

# User's tasks
num_tasks = st.number_input("Select the number of tasks", min_value=1, max_value=20, value=1, step=1)
story += f" He has {num_tasks} number of tasks."
for i in range(1, int(num_tasks) + 1):
    if (len(can_confirm) <= i):
        can_confirm.append(False)
    task_desc = st.text_area("Task Description " + str(i), placeholder = "Type in your task description here", key="task_desc" + str(i))
    if (task_desc == ""):
        can_confirm[i] = False
        st.write("This is a required field")
    else:
        can_confirm[i] = True
        story += f" Task {str(i)}: {task_desc}."
    task_hours = st.number_input("Type in the number of hours task " + str(i) + " takes", min_value=0.5, max_value=float(20), value=0.5, step=0.5, key="task_hours" + str(i))
    story += f" This task takes {task_hours} amount of hours."
story += f" Assume he needs at least 0.5 hours of break today. Plan an optimal schedule for him."
st.write(story)

# Confirmation button, only activated when the conditions are fulfilled
if (False not in can_confirm):
    pressed = st.button("Submit")
    # If pressed, we then want to take the current input and plan the schedule for the user using openai
    # Our current input would be the story variable
    res_box = st.empty()
    completions = openai.ChatCompletion.create(model="gpt-4", messages=[
                        {"role": "assistant",
                        "content": story,
                        }],
                        temperature=0.5,
                        max_tokens=1000,
                        frequency_penalty=0.0,)
    result = completions.choices[0].message.content
    res_box.write(result)



st.write("*Copyright © 2023 TPJC - Harry, Brendan, Yong Jun, Ryan*") 