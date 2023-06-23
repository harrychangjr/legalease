import streamlit as st
from PIL import Image


legalease = Image.open("assets/LegalEase.jpg")
banner = Image.open("assets/banner.jpg")

st.set_page_config(page_title="LegalEase - Home", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
#st.sidebar.title("LegalEase")
st.sidebar.image(legalease)
st.image(banner)

#st.header("LegalEase")
st.subheader("Home")
#st.write("*Empowering lawyers in hybrid work environments with mental health support & optimal task scheduling*")
st.markdown("""
Hello there!

We are a group of NUS students who are aiming to solve the issue of mental health for lawyers struggling in hybrid working environments. 
Bonded by our alma mater, Tampines Junior College (TPJC), we have built several key features which we believe can tackle the problem at hand.

**Key features**: 
- *Daily Planner (with OpenAI)* 
- *Mood Tracker with Journal*
- *Peer Support (Discussion Forum)*
- *Mental Health Resources*

You may also check out our demo video below, as a quick walkthrough of our application. Enjoy!

~ Team TPJC, SMU-LIT Hackathon 2023

""")

#st.video
st.write("*Video updated as of 23 June 2023, to be published*")

st.write("*Copyright © 2023 TPJC - Harry, Brendan, Yong Jun, Ryan*") 