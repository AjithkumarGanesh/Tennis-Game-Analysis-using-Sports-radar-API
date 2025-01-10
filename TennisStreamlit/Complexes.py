import mysql.connector
import streamlit as st
import pandas as pd
from PIL import Image

try:
    # Title of the page
    st.title("Welcome to Complexes Endpoint Dashboard")
    st.write("\n")
    st.subheader("Here you can find all the tables related to Complexes Endpoint")

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
    overallcountquery = "select * from venues;"
    cursor.execute(overallcountquery)
    overallresult = cursor.fetchall()
    # Convert to DataFrame
    overalldataframe = pd.DataFrame(overallresult, columns=cursor.column_names)
    data1=overalldataframe["venue_id"].count()
    st.sidebar.metric(label="TOTAL NO OF VENUES",value=data1)
    
    # Sidebar filter
    st.sidebar.title("List Venues based on Country")
    st.sidebar.subheader("Country Filter")
    filter_type = st.sidebar.selectbox("Select Country Name", ["Select any one","Chile", "Russia", "Portugal"])

    # Fetch and display results based on the selected filter
    if filter_type=="Select any one":
        st.sidebar.subheader("No Selections made")
    else:
        st.sidebar.subheader("Filtered Results")
        filterquery = "SELECT venue_name AS Venue_Name FROM venues WHERE country_name = %s"
        cursor.execute(filterquery, (filter_type,))
        filterresult = cursor.fetchall()

        # Convert to DataFrame
        filterdataframe = pd.DataFrame(filterresult, columns=["Venue Name"])
        st.sidebar.table(filterdataframe)

    # Execute the query
    query1 = """SELECT complexes.complex_name, COUNT(venues.venue_name) as venue_count
                FROM complexes
                left join venues 
                on complexes.complex_id=venues.complex_id
                GROUP BY complexes.complex_name 
                ORDER BY venue_count desc;
              """
    cursor.execute(query1)
    result1 = cursor.fetchall()

    # Convert to DataFrame
    dataframe1 = pd.DataFrame(result1, columns=cursor.column_names)


    # Execute the query
    query2 = """select venues.venue_name,complexes.complex_name from venues inner join complexes on venues.complex_id = complexes.complex_id;"""
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
            st.write("Table 1: Count the number of venues in each complex")
            st.dataframe(dataframe1)

        # Display the second table in the second column
        with col2:
            st.write("Table 2: List all venues along with their associated complex name")
            st.dataframe(dataframe2)
    else:
        st.write("No data available.")

    # Execute the query
    query3 = """select * from venues where country_name = "Chile" or country_code = "CHL";"""
    cursor.execute(query3)
    result3 = cursor.fetchall()

    # Convert to DataFrame
    dataframe3 = pd.DataFrame(result3, columns=cursor.column_names)


    # Execute the query
    query4 = """select venue_id,venue_name,timezone from venues;"""
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
            st.write("Table 3: Get details of venues in a specific country (e.g., Chile)")
            st.dataframe(dataframe3)

        # Display the fourth table in the second column
        with col4:
            st.write("Table 4: Identify all venues and their timezones from the list of Venues")
            st.dataframe(dataframe4)
    else:
        st.write("No data available.")

    # Execute the query
    query5 = """select venues.complex_id,complexes.complex_name,count(venues.venue_id) as venue_count 
                from complexes 
                inner join venues
                on complexes.complex_id=venues.complex_id
                group by venues.complex_id,complexes.complex_name having count(venues.venue_id)>1; """
    cursor.execute(query5)
    result5 = cursor.fetchall()

    # Convert to DataFrame
    dataframe5 = pd.DataFrame(result5, columns=cursor.column_names)


    # Execute the query
    query6 = """SELECT country_name, GROUP_CONCAT(venue_name SEPARATOR ' | ') AS venues FROM venues GROUP BY country_name;"""
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
            st.write("Table 5: Find complexes that have more than one venue")
            st.dataframe(dataframe5)

        # Display the sixth table in the second column
        with col6:
            st.write("Table 6: List venues grouped by country from venues table")
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
