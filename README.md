# Tennis-Game-Analysis-using-Sports-radar-API

This project is a comprehensive Tennis Analytics Dashboard built using Streamlit. It provides interactive data visualization for Competitions, Complexes, and Doubles Competitor Rankings, along with a centralized Home Page for easy navigation.

Project Overview:
1. Data Acquisition and Processing

API Integration: Data was sourced from the SportsRadar API. JSON responses were retrieved, converted into Python dictionaries, and further transformed into pandas DataFrames for     structured table-like representation.
Data Export: DataFrames were exported as .csv files using the .to_csv() method, enabling efficient storage and reuse.

2. Database Setup

Database Management: The project leverages MySQL Workbench for database storage.

Tables Created: 
Six tables were designed to store and organize data:
competitions
complexes
venues
categories
competitors
competitor_rankings

CSV Import:
The .csv files generated during the data processing phase were imported into the respective MySQL tables.

3. Data Visualization with Streamlit

Four Streamlit scripts were developed for interactive data visualization:

Home: A central dashboard to navigate across various analytics pages.
Competition: Insights and analytics on tennis competitions.
Complexes: Visualization of data related to tennis complexes.
Doubles Competitor Rankings: Detailed rankings of doubles competitors.

4. Folder Structure
Root path:
Home.py
Competitions_Endpoint.py
Competitor_Rankings_Endpoint.py
Complexes_Endpoint.py
