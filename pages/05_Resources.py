import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu

legalease = Image.open("assets/LegalEase.jpg")
banner = Image.open("assets/banner.jpg")

st.set_page_config(page_title="LegalEase - Resources", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
#st.sidebar.title("LegalEase")
st.sidebar.image(legalease)
st.image(banner)

lawsoc = Image.open("assets/lawsoc.jpg")
sos = Image.open("assets/sos.jpg")
samh = Image.open("assets/samh.jpg")
nams = Image.open("assets/nams.jpg")
eap = Image.open("assets/eap.jpg")
intellect = Image.open("assets/intellect.jpg")
ifc = Image.open("assets/ifc.jpg")
tfc = Image.open("assets/tfc.jpg")
mindfi = Image.open("assets/mindfi.jpg")
safespace = Image.open("assets/safespace.jpg")
kura = Image.open("assets/kura.jpg")
oura = Image.open("assets/oura.jpg")
applewatch = Image.open("assets/applewatch.jpg")
thync = Image.open("assets/thync.jpg")
muse = Image.open("assets/muse.jpg")
zeeq = Image.open("assets/zeeq.jpg")
apollo = Image.open("assets/apollo.jpg")


#st.header("LegalEase")
st.subheader("Resources")

st.write("*Feeling burnt out and need help? Here are some mental health resources to get you started!*")

tab1, tab2, tab3 = st.tabs(["Websites", "Applications", "Devices"])

with tab1:
    st.write("The organisations and/or programmes below are targeted to assist lawyers who may be struggling with their work commitments, especially with the post-COVID transition to a hybrid working environment. Do check them out below!")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(lawsoc)
        with text_column:
            st.subheader("[Law Society of Singapore](https://www.lawsociety.org.sg/the-law-society/support-schemes/)")
            st.write("The Law Society offers various support services for lawyers, including a Lawyers' Assistance Programme (LAP) which provides confidential counseling and support. They also have a Wellness Programme that focuses on promoting mental well-being within the legal profession.")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(sos)
        with text_column:
            st.subheader("[Samaritans of Singapore (SOS)](https://www.sos.org.sg/)")
            st.write("SOS is a non-profit organization that provides emotional support and crisis intervention services. They have a 24-hour helpline (1800-221-4444) that offers a listening ear and guidance to individuals who are in distress.")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(samh)
        with text_column:
            st.subheader("[Singapore Association of Mental Health (SAMH)](https://www.samhealth.org.sg/)")
            st.write("SAMH provides a range of mental health services, including counseling and support groups. They offer individual counseling services, as well as group therapy programs that can help lawyers connect with others who may be facing similar challenges.")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(nams)
        with text_column:
            st.subheader("[National Addictions Management Service (NAMS)](https://www.nams.sg/Pages/default.aspx)")
            st.write("NAMS is a specialized service under the Institute of Mental Health (IMH) that focuses on the management and treatment of addictions. If a lawyer is struggling with substance abuse or addiction-related issues, NAMS can provide assessment, counseling, and treatment options.")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(eap)
        with text_column:
            st.subheader("[Employee Assistance Program (EAP)](https://scc.sg/e/employee-assistance-programme/)")
            st.write("Some law firms in Singapore offer Employee Assistance Programs that provide confidential counseling and support services for their employees. Lawyers can inquire within their organizations to see if such a program exists.")
            

with tab2:
    st.write("The following applications aim to provide additional support to lawyers who wish to seek help either anonymously via peer support of through professional help. Do check them out below!")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(intellect)
        with text_column:
            st.subheader("[Intellect](https://intellect.co/)")
            st.write("For HR professionals looking to proactively care for employee wellbeing, Intellect takes the guesswork out with our research-proven mental health platform to nurture a thriving workplace. Speak with behavioural health coaches, work with licensed psychologists, or take on self-guided programs, entirely within a single platform.")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(ifc)
        with text_column:
            st.subheader("[I'm Friendly Co.](https://imfriendlyco.com/)")
            st.write("An anonymous platform where any youth or young adult can turn to and find emotional support, a listening ear, a friend in time of need.")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(tfc)
        with text_column:
            st.subheader("[ThoughtFullChat](https://www.thoughtfull.world/)")
            st.write("A subscription-based mobile platform that empowers users to proactively engage with their mental health via self-serve tools and 1-on-1 daily bite-sized coaching with certified mental health professionals.")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(mindfi)
        with text_column:
            st.subheader("[MindFi](https://mindfi.co/)")
            st.write("MindFi provides you with a centralized platform to integrate all your initiatives in one structured and trackable program so that you can deploy your best wellbeing strategy.")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(safespace)
        with text_column:
            st.subheader("[Safe Space™](https://safespace.sg/)")
            st.write("Safe Space™ offers live support and online resources that anyone seeking to enhance their mental wellness can use.")

    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(kura)
        with text_column:
            st.subheader("[Kura Kura](https://kurakura.io/)")
            st.write("Discover Kura Kura, your digital companion fostering emotional vulnerability. Engage in our interactive games and prompts, encouraging open expression.")

with tab3:
    st.write("The following wearable items can aid mental health by monitoring sleep patterns, tracking heart rate variability, and providing tools for stress management and relaxation. Do check them out below!")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(oura)
        with text_column:
            st.subheader("[Oura Ring](https://ouraring.com/)")
            st.write("*The Oura Ring aids mental health by monitoring sleep patterns, tracking heart rate variability (HRV), and providing personalized recommendations for optimizing sleep and recovery.*")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(applewatch)
        with text_column:
            st.subheader("[Apple Watch](https://www.apple.com/sg/watch/)")
            st.write("*The Apple Watch contributes to mental health by monitoring heart rate, offering guided breathing exercises for stress management, promoting physical activity, and providing access to mindfulness and meditation apps.*")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(thync)
        with text_column:
            st.subheader("[Thync](https://thync.com/)")
            st.write("*Thync is a device that aims to enhance mental well-being through neurostimulation, using electrical currents to promote relaxation or boost energy levels.*")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(muse)
        with text_column:
            st.subheader("[Muse](https://choosemuse.com/)")
            st.write("*The Muse headband helps with mental health by measuring brainwave activity during meditation, providing real-time feedback to improve focus and relaxation.*")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(zeeq)
        with text_column:
            st.subheader("[ZEEQ Smart Pillow](https://sleepgadgets.io/zeeq-smart-pillow/)")
            st.write("*The ZEEQ Smart Pillow contributes to mental health by monitoring sleep quality, offering features like snoring detection and gentle vibrations to encourage better sleep habits.*")
    with st.container():
        image_column, text_column = st.columns((1,3))
        with image_column:
            st.image(apollo)
        with text_column:
            st.subheader("[Apollo Neuro](https://apolloneuro.com/)")
            st.write("*Apollo Neuro is a wearable device that utilizes gentle vibrations to promote stress reduction, relaxation, and improved sleep by activating the body's natural responses and helping regulate the nervous system.*")

st.write("*Copyright © 2023 TPJC - Harry, Brendan, Yong Jun, Ryan*") 