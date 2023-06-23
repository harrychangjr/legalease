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
import nltk
nltk.download('vader_lexicon')

  

legalease = Image.open("assets/LegalEase.jpg")
banner = Image.open("assets/banner.jpg")

st.set_page_config(page_title="LegalEase - Mood Tracker", page_icon = "👨🏻‍⚖️", layout = "centered", initial_sidebar_state = "auto")
st.sidebar.image(legalease)
st.image(banner)

#st.header("LegalEase")
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
mood = st.slider("Mood: 1 (lowest) - 10 (highest)", 1, 10)
journal = st.text_area("Journal Entry")

# Add mood and journal data to DataFrame
if st.button("Add Entry"):
    data = data.append({"Date": str(date), "Mood": mood, "Journal": journal}, ignore_index=True)
    data.to_csv(data_file, index=False)  # Save the data to the file
    st.success("Entry added successfully!")

# Clear data button
if st.button("Clear Data"):
    data = pd.DataFrame(columns=["Date", "Mood", "Journal"])
    if os.path.exists(data_file):
        os.remove(data_file)
    st.warning("Mood data cleared!")

# Display mood and journal data table
#st.subheader("Mood and Journal Entries")
#st.dataframe(data)

# Display mood and journal data table
#st.subheader("Mood and Journal Entries")
#st.dataframe(data)

# Perform sentiment analysis on journal entries
if not data.empty:
    sid = SentimentIntensityAnalyzer()
    data["Sentiment Score"] = data["Journal"].apply(lambda x: sid.polarity_scores(x)["compound"])
    st.subheader("Mood and Sentiment Analysis of Journal Entries")
    st.dataframe(data[["Date", "Mood", "Journal", "Sentiment Score"]])

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
st.subheader("Scores Analysis (R-squared value)")
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

st.subheader("Understanding the Metrics")
tab1, tab2 = st.tabs(["Sentiment Score", "R-squared Value"])
with tab1:
    st.write("Sentiment scoring is a way to understand the emotions or attitudes expressed in text using special computer techniques. It involves analyzing words and phrases in the text and assigning them sentiment values (like positive, negative, or neutral). By combining these values, an overall sentiment score is calculated. This process often relies on pre-built sentiment models that contain information about how different words are associated with specific sentiments. The NLTK library is commonly used to perform this analysis by handling tasks like preparing the text, breaking it into meaningful parts, and matching words with sentiment values. However, it's important to keep in mind that sentiment analysis is not perfect, and the accuracy of the scores can vary depending on factors like the quality of the sentiment model and the specific context of the text being analyzed.")
with tab2:
    st.write("The R-squared value is a statistical measure that tells us how well the mood scores can explain the sentiment scores in the mood tracker. It represents the percentage of the variation in the sentiment scores that can be understood by changes in the mood scores. A higher R-squared value means that the mood scores provide a better understanding of the sentiment scores. However, it's important to remember that the R-squared value does not tell us about causation or the full picture of the relationship between mood and sentiment. It's just one way to assess how well the mood scores fit the sentiment scores in the analysis.")
