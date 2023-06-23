import streamlit as st
import datetime
from PIL import Image

legalease = Image.open("assets/LegalEase.jpg")
banner = Image.open("assets/banner.jpg")

# Page configuration
st.set_page_config(
    page_title="LegalEase - Peer Support",
    page_icon="👨‍⚖️",
    layout="centered",
    initial_sidebar_state="auto",
)
st.sidebar.image(legalease)
st.image(banner)


# Set header and subheader of the page
st.subheader("Peer Support")
st.write("*A platform for lawyers to connect, share experiences and support each other.*")

# Fake Discussion and Comment data
discussions = [
    {
        "id": 1,
        "title": "Dealing with Stress",
        "username": "JohnDoe",
        "timestamp": "June 22, 2023 14:32",
        "text": "Stress is common in our profession. How do you guys manage it?",
        "comments": [],
        "likes": 5,
    },
    {
        "id": 2,
        "title": "Work-Life Balance",
        "username": "LawyerJane",
        "timestamp": "June 21, 2023 17:20",
        "text": "How do you maintain a healthy work-life balance?",
        "comments": [],
        "likes": 2,
    },
]

# Fake Resources data
resources = [
    {"title": "Stress Management Guide", "link": "www.resource1.com"},
    {"title": "Maintaining Work-Life Balance", "link": "www.resource2.com"},
]


# Function to display a discussion
def display_discussion(discussion):
    st.subheader(discussion["title"])
    st.write(f"Posted by {discussion['username']} on {discussion['timestamp']}")
    st.write(discussion["text"])
    if st.button("Like", key=f"like_{discussion['id']}"):
        discussion["likes"] += 1
    st.write(f"Likes: {discussion['likes']}")

    st.write("Comments:")
    for comment in discussion["comments"]:
        st.text(comment)
    comment_text = st.text_input(
        "Write a comment...", key=f"comment_{discussion['id']}"
    )
    if st.button("Post Comment", key=f"post_{discussion['id']}"):
        discussion["comments"].append(
            f"{st.session_state.username if 'username' in st.session_state else 'anonymous'}: {comment_text}"
        )


# Function to display a resource
# def display_resource(resource):
    # st.subheader(resource["title"])
    # st.write(f"[Link]({resource['link']})")


# Sidebar for creating a new discussion
with st.sidebar:
    st.subheader("Start a new discussion")
    discussion_title = st.text_input("Discussion Title")
    discussion_text = st.text_area("Your Discussion")
    if st.button("Post Discussion"):
        # Add the discussion to the list
        discussions.append(
                {
                    "id": len(discussions) + 1,
                    "title": discussion_title,
                    "username": st.session_state.get('username', 'anonymous'),
                    "timestamp": datetime.datetime.now().strftime("%B %d, %Y %H:%M"),
                    "text": discussion_text,
                    "comments": [],
                    "likes": 0,
                }
            )
        st.success("Your discussion has been posted.")

# Main Page
# Display the discussions
st.header("Discussion Forum")
for discussion in reversed(
    discussions
):  # Display the discussions in reverse order (latest first)
    display_discussion(discussion)

# Display the resources
#st.header("Resources")
#for resource in resources:
    #display_resource(resource)
