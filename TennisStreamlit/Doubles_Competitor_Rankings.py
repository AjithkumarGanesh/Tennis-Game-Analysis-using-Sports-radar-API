import mysql.connector
import streamlit as st
import pandas as pd
from PIL import Image

try:
    # Title of the page
    st.title("Welcome to Doubles Competitor Rankings Endpoint Dashboard")
    st.write("\n")
    st.subheader("Here you can find all the tables related to Doubles Competitor Rankings Endpoint")

    # Sidebar with a logo
    st.sidebar.image("Logo.jpeg", use_container_width=True)  # Replace with our logo file path
        
    #Establish Connection
    db = mysql.connector.connect(
        host="localhost",  # Replace with our host
        user="root",       # Replace with our username
        password="aji",    # Replace with our password
        database="tennisdatadb"  # Replace with our database name
    )
    print("Connection successful!")
    cursor = db.cursor()
    
    # Overall Competition count
    overallcountquery = "select * from competitor;"
    cursor.execute(overallcountquery)
    overallresult = cursor.fetchall()
    # Convert to DataFrame
    overalldataframe = pd.DataFrame(overallresult, columns=cursor.column_names)
    data1=overalldataframe["name"].count()
    st.sidebar.metric(label="TOTAL NO OF COMPETITORS",value=data1)
    
    # Sidebar filter
    st.sidebar.title("List Competitors based on Country")
    st.sidebar.subheader("Country Filter")
    filter_type = st.sidebar.selectbox("Select Country Name", ["Select any one","Argentina", "Germany", "India"])

    # Fetch and display results based on the selected filter
    if filter_type=="Select any one":
        st.sidebar.subheader("No Selections made")
    else:
        st.sidebar.subheader("Filtered Results")
        filterquery = "SELECT name AS Competitor_Name FROM competitor WHERE country = %s"
        cursor.execute(filterquery, (filter_type,))
        filterresult = cursor.fetchall()

        # Convert to DataFrame
        filterdataframe = pd.DataFrame(filterresult, columns=["Competitor Name"])
        st.sidebar.table(filterdataframe)

    # Execute the query
    query1 = """select competitor.competitor_id,competitor.name,competitor_rankings.rank,competitor_rankings.points
                from competitor
                inner join competitor_rankings
                on competitor.competitor_id=competitor_rankings.competitor_id;
             """
    cursor.execute(query1)
    result1 = cursor.fetchall()

    # Convert to DataFrame
    dataframe1 = pd.DataFrame(result1, columns=cursor.column_names)


    # Execute the query
    query2 = """select competitor.competitor_id,competitor.name,competitor_rankings.`rank`, competitor_rankings.movement
                from competitor
                inner join competitor_rankings
                on competitor.competitor_id=competitor_rankings.competitor_id 
                where competitor_rankings.movement='0';"""
    cursor.execute(query2)
    result2 = cursor.fetchall()

    # Convert to DataFrame
    dataframe2 = pd.DataFrame(result2, columns=cursor.column_names)

    # Display the data side by side in columns
    if not dataframe1.empty and not dataframe2.empty:
        # Create two columns
        col1, col2 = st.columns(2)

        # Display the first table in the first column
        with col1:
            st.write("Table 1: Get all competitors with their rank and points")
            st.dataframe(dataframe1)

        # Display the second table in the second column
        with col2:
            st.write("Table 2: List competitors with no rank movement (stable rank)")
            st.dataframe(dataframe2)
    else:
        st.write("No data available.")

    # Execute the query
    query3 = """select country, count(name) as Competitors_per_Country from competitor group by country;"""
    cursor.execute(query3)
    result3 = cursor.fetchall()

    # Convert to DataFrame
    dataframe3 = pd.DataFrame(result3, columns=cursor.column_names)


    # Execute the query
    query4 = """select competitor.competitor_id,competitor.name,competitor_rankings.rank,competitor_rankings.points
                from competitor
                inner join competitor_rankings
                on competitor.competitor_id=competitor_rankings.competitor_id
                where competitor_rankings.rank>="1" and competitor_rankings.rank<="5"
                order by `rank`,points desc limit 5;"""
    cursor.execute(query4)
    result4 = cursor.fetchall()

    # Convert to DataFrame
    dataframe4 = pd.DataFrame(result4, columns=cursor.column_names)

    # Display the data side by side in columns
    if not dataframe3.empty and not dataframe4.empty:
        # Create two columns
        col3, col4 = st.columns(2)

        # Display the third table in the first column
        with col3:
            st.write("Table 3: Count the number of competitors per country")
            st.dataframe(dataframe3)

        # Display the fourth table in the second column
        with col4:
            st.write("Table 4: Find competitors ranked in the top 5 from rankings list")
            st.dataframe(dataframe4)
    else:
        st.write("No data available.")

    # Execute the query
    query5 = """select competitor.country,count(competitor.name) as Total_Competitors_from_a_country, sum(competitor_rankings.points) as Total_Points_Scored
                from competitor
                inner join competitor_rankings
                on competitor.competitor_id=competitor_rankings.competitor_id 
                Group by competitor.country having competitor.country="India";"""
    cursor.execute(query5)
    result5 = cursor.fetchall()

    # Convert to DataFrame
    dataframe5 = pd.DataFrame(result5, columns=cursor.column_names)


    # Execute the query
    query6 = """select competitor.competitor_id,competitor.name,competitor_rankings.`rank`,competitor_rankings.points as max_points_scored
                from competitor
                inner join competitor_rankings
                on competitor.competitor_id=competitor_rankings.competitor_id
                where competitor_rankings.points= (select max(points) from competitor_rankings);"""
    cursor.execute(query6)
    result6 = cursor.fetchall()

    # Convert to DataFrame
    dataframe6 = pd.DataFrame(result6, columns=cursor.column_names)

    # Display the data side by side in columns
    if not dataframe5.empty and not dataframe6.empty:
        # Create two columns
        col5, col6 = st.columns(2)

        # Display the fifth table in the first column
        with col5:
            st.write("Table 5: Get the total points of competitors from a specific country (e.g., India)")
            st.dataframe(dataframe5)

        # Display the sixth table in the second column
        with col6:
            st.write("Table 6: Find competitors with the highest points in the current week")
            st.dataframe(dataframe6)
            
    else:
        st.write("No data available.")

    

except mysql.connector.Error as e:
    print(f"Connection error: {e}")
finally:
    if cursor:
            cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()