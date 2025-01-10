import streamlit as st
import pandas as pd
import mysql.connector
from PIL import Image

# Sidebar with a logo
st.sidebar.image("Logo.jpeg", use_container_width=True)  # Replace with our logo file path

# Home Page (Landing Page Content)
# Load your background image
bg_image = Image.open("BgImage.jpeg")  

# Create two columns
col1, col2 = st.columns([1, 2])  # The number values control the width ratio (1:2 in this case)

# Display image in the first column
with col1:
    st.image(bg_image, use_container_width=True)

# Display text in the second column
with col2:
    st.title("Tennis Sport Radar")
    st.write("\n")
    st.write("Game, Set, Data: Winning Insights at Your Fingertips.")
    
# Title of the page
st.title("Welcome to Tennis Sport Radar!")
st.write("\n")

# Introduction
st.subheader("Unlock the Power of Tennis Data for Winning Insights")
st.write(""" Tennis Sport Radar is a cutting-edge platform designed for tennis enthusiasts, players, and analysts who want to take their game to the next level. Our website brings you comprehensive data analysis, insights, and tools to track performance, identify trends, and predict outcomes in the world of tennis.
""")

# Features
st.subheader("Features")
st.write("""
- **Comprehensive Match Statistics**  
 Dive deep into match statistics such as aces, double faults, serve speeds, winners, errors, and more. Visualize player performance over time to spot trends and areas for improvement.

- **Player Comparison Tools**  
  Compare top players’ statistics head-to-head in real-time. Identify strengths and weaknesses, and gain valuable insights into how different players approach their game.

- **Predictive Analytics**  
  Using advanced algorithms, our system analyzes historical data and player performance metrics to predict match outcomes, tournament winners, and player form.

- **Interactive Data Visualizations**  
  Explore interactive charts, graphs, and heatmaps to better understand key match statistics. Get instant access to visual insights and comparisons.

- **Detailed Player Profiles**  
  Explore comprehensive profiles of professional tennis players, with career stats, performance trends, and match-by-match breakdowns.
""")

# Why Choose Section
st.subheader("Why Choose Tennis Sport Radar?")
st.write("""
- **Data-Driven Decision Making**  
  Whether you’re a coach looking to optimize your player’s training, a fan analyzing match statistics, or a player trying to improve performance, our platform provides you with the tools you need to make data-driven decisions.

- **Stay Ahead of the Competition**  
  With the latest updates and cutting-edge analytics, you'll always stay one step ahead. Monitor player performance, study matchups, and gain a competitive advantage in your betting or analysis.

- **Engage with the Tennis Community**  
  Share insights, compare stats, and discuss trends with a community of passionate tennis fans and experts.
""")

# Call to action
st.subheader("Get Started")
st.write("""
Sign up now to get started with Tennis Sport Radar!  
Start exploring player stats, match analytics, and predictive data tools to enhance your tennis experience.
""")

    



