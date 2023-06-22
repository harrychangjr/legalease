import streamlit as st
from PIL import Image
from streamlit_option_menu import option_menu
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import seaborn as sns
from scipy import stats
from nltk.sentiment import SentimentIntensityAnalyzer

legalease = Image.open("assets/LegalEase.jpg")

st.set_page_config(page_title="LegalEase - Mood Tracker", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
st.sidebar.image(legalease)

st.header("LegalEase")
st.subheader("Mood Tracker with Journal")
st.write("*Track your daily mood, journal entries, and visualize mood trends over time!*")

# File paths
data_file = "mood_data.csv"

# Create a DataFrame to store mood and journal data
if not os.path.exists(data_file):
    data = pd.DataFrame(columns=["Date", "Mood", "Journal"])
else:
    data = pd.read_csv(data_file)

# Input form to track mood and journal entry
date = st.date_input("Date")
mood = st.slider("Mood (1-10)", 1, 10)
journal = st.text_area("Journal Entry")

# Add mood and journal data to DataFrame
if st.button("Add Entry"):
    data = data.append({"Date": str(date), "Mood": mood, "Journal": journal}, ignore_index=True)
    data.to_csv(data_file, index=False)  # Save the data to the file
    st.success("Entry added successfully!")

# Display mood and journal data table
st.subheader("Mood and Journal Entries")
st.dataframe(data)

# Perform sentiment analysis on journal entries
if not data.empty:
    sid = SentimentIntensityAnalyzer()
    data["Sentiment Score"] = data["Journal"].apply(lambda x: sid.polarity_scores(x)["compound"])
    st.subheader("Sentiment Analysis of Journal Entries")
    st.dataframe(data[["Date", "Journal", "Sentiment Score"]])

# Display mood trends and sentiment scores over time
st.subheader("Mood Trends and Sentiment Scores Over Time")
if not data.empty:
    data["Date"] = pd.to_datetime(data["Date"])
    data.set_index("Date", inplace=True)
    data.sort_index(inplace=True)
    plt.figure(figsize=(10, 6))
    
    # Line plot for mood
    plt.plot(data.index, data["Mood"], label="Mood")
    plt.xlabel("Date")
    plt.ylabel("Mood")
    
    # Scatter plot for mood data
    plt.scatter(data.index, data["Mood"], color="red", label="Mood Data")
    
    # Add average line and annotate average value for mood
    avg_mood = data["Mood"].mean()
    plt.axhline(avg_mood, color="red", linestyle="--", label="Average Mood")
    plt.text(data.index[-1], avg_mood, f" Avg: {avg_mood:.2f}", va="center", ha="right", color="red")
    
    # Create secondary y-axis for sentiment score
    ax2 = plt.gca().twinx()
    
    # Line plot for sentiment score
    ax2.plot(data.index, data["Sentiment Score"], label="Sentiment Score", color="green")
    ax2.set_ylabel("Sentiment Score")
    
    plt.title("Mood Trends and Sentiment Scores")
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Display x-axis on a daily basis
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))  # Format x-axis date display
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    
    plt.legend(loc="upper left")
    st.pyplot(plt)
else:
    st.info("Add mood data to visualize trends.")

# Create scatter plot with regression line
plt.figure(figsize=(8, 6))
sns.regplot(data=data, x="Mood", y="Sentiment Score")
plt.xlabel("Mood")
plt.ylabel("Sentiment Score")
plt.title("Relationship between Mood and Sentiment Score")
plt.grid(True)

# Calculate R-square value
x = data["Mood"]
y = data["Sentiment Score"]
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
r_squared = r_value ** 2

# Add R-square label
plt.text(x.min(), y.max(), f"R-square = {r_squared:.2f}", ha='left', va='top')

st.pyplot(plt)