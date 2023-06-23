import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

legalease = Image.open("assets/LegalEase.jpg")
banner = Image.open("assets/banner.jpg")

st.set_page_config(page_title="LegalEase - About Us", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
#st.sidebar.title("LegalEase")
st.sidebar.image(legalease)
st.image(banner)

# Use the following line to include your style.css file
#st.markdown('<style>' + open('style.css').read() + '</style>', unsafe_allow_html=True)

#st.header("LegalEase")
st.subheader("About Us!")

harry = Image.open("assets/harry.jpg")
brendan = Image.open("assets/brendan.jpg")
yj = Image.open("assets/yj.jpg")
ryan = Image.open("assets/ryan.jpg")

selected_options = ["Overview", "Summary", "Our Team", "References"]
selected = st.selectbox("Which section would you like to read?", options = selected_options)
st.write("Current selection:", selected)
if selected == "Overview":
    st.subheader("Overview")
    st.markdown("""
    **Overall Theme: Bridging the Tech-Law Divide**

    **Chosen Theme and Statement: Hybrid Working - Mental Health**

    Problem Statement: Fully remote work arrangements during the pandemic has led to many lawyers feeling burnt out. This was in part due to the lack of social interaction and the subsequent feelings of isolation, alongside the blurring of lines between rest and work. How might we then utilise technology to mitigate such risks and help lawyers with their mental health when it comes to hybrid working arrangements?

    """)

elif selected == "Summary":
    st.subheader("Summary")
    st.markdown("""
    For SMU-LIT Hackathon 2023, we have chosen the theme of Hybrid Working, which requires us to ideate an application to support the mental health of lawyers working in hybrid arrangements.

    To address this problem statement, we have come up with *LegalEase*, a web application that empowers lawyers in hybrid work environments with mental health support & optimal task scheduling.
    
    **Inspiration**

    The COVID-19 pandemic has drastically changed the way we work, and lawyers are no exception. Remote work arrangements have led to feelings of isolation, burnout, and stress, negatively impacting mental health. Drawing on our experiences as university students familiar with these challenges, we want to create a solution that improves the mental well-being of lawyers working in hybrid environments.

    **What it does**

    Our application will consist of four main features:

    - **Daily Planner:** Powered by OpenAI, the AI suggests an optimal schedule based on the tasks inputted by the lawyer, taking into account the need for regular breaks and personal time to prevent burnout.

    - **Mood Tracker:** Users can log their mood and feelings daily, which can be visualized over time to help them understand their emotional patterns.

    - **Peer Support:** Users can rely on other fellow lawyers for advice, if needed, for mental health support and advice in the form of a discussion forum. They will get to interact with one another, similar to typical social media or forum posts such as Facebook or Twitter posts.

    - **Mental Health Resources:** Curated content and resources on mental health support for lawyers.

    **How we built it**

    We used Streamlit, HTML and CSS as our front-end for our web application, and utilised the OpenAI API for our back-end.

    **What makes our solution stand out**

    With our AI-powered daily planner, lawyers can relieve their burden in case/task management, especially at times when they are feeling overwhelmed by the amount of work they need to deal with.
    To supplement this, we have also built a mood tracker, which provides a unique data-driven approach for lawyers to monitor their mental health on a daily basis. 

    **Some key challenges we faced**

    A key issue that we've faced is the transition from our typical skillset of HTML/CSS/Javascript to Streamlit, as we wanted to fully utilise the OpenAI API for easier facilitation of the back-end. In addition, we were also new to utilising Firebase to store user data for our login system, to track user history of previous inputs using our app.

    **What's next for LegalEase**

    We aim to continue refining the AI's task scheduling capabilities and explore additional features that further support the mental well-being of legal professionals in a hybrid working environment. This could include virtual group activities, guided meditation sessions, and more. Also, we aim to implement a login system using either Firebase or SingPass so that users can save their previous records in a safe manner should they need to check their personal data.

    **Built with**

    `Python` `Streamlit` `HTML` `CSS` `OpenAI API`

    Github repo: https://github.com/harrychangjr/legalease

    """)

elif selected == "Our Team":
    st.subheader("Our Team")
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(harry)
        with text_column:
            st.subheader("Harry Chang")
            st.write("*NUS Data Science and Analytics '24*")
            st.markdown("""
            Role: Front-end, Branding Assets, Copywriting

            `Python` `HTML` `CSS` `Streamlit` `R` `Java` `Figma`
            """)
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(brendan)
        with text_column:
            st.subheader("Brendan Cheong")
            st.write("*NUS Business Analytics and Economics '24*")
            st.markdown("""
            Role: Front-end, Back-end

            `Python` `HTML` `CSS` `Streamlit` `Javascript` `React`
            """)
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(yj)
        with text_column:
            st.subheader("Tay Yong Jun")
            st.write("*NUS Law '25*")
            st.markdown("""
            Role: Legal Advisor, User Tester

            """)
    with st.container():
        image_column, text_column = st.columns((1.5,5))
        with image_column:
            st.image(ryan)
        with text_column:
            st.subheader("Ryan Tan")
            st.write("*NUS Business Analytics '24*")
            st.markdown("""
            Role: Back-end

            `CPP` `Java` `Python` `HTML` `CSS` `Javascript` `Streamlit` `Firebase`
            """)

elif selected == "References":
    st.subheader("References")
    st.markdown("""
            - Streamlit API Documentation: https://docs.streamlit.io/ 

            - OpenAI API Documentation: https://openai.com/blog/openai-api 
            """)

st.write("*Copyright © 2023 TPJC - Harry, Brendan, Yong Jun, Ryan*") 

