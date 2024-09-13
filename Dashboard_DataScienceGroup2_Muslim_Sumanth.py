# Importing necessary libraries for data handling, visualization, and dashboard creation
import plotly.express as px
import pandas as pd
import streamlit as st
import matplotlib as plt
import seaborn as sns

####################################################################################################

# Configuring the dashboard with a title, icon, and layout
st.set_page_config(page_title="Income Distribution Dashboard", page_icon=":bar_chart:", layout="wide")

# Setting the title of the dashboard
st.title("Income Distribution Dashboard")

# Adding a subtitle or description to the dashboard
st.markdown("Data Science Group 2")

# Sidebar configuration for file upload
with st.sidebar:
    st.header("Configuration")  # Header for sidebar
    uploaded_file = st.file_uploader("Choose a file")  # Upload CSV file for analysis

# Display message if no file is uploaded, then stop execution
if uploaded_file is None:
    st.info(" Upload a file through config", icon="ℹ️")
    st.stop()

###################################################################################################

# Caching the data loading function to avoid reloading the data on every interaction
@st.cache_data
def load_data(path: str):
    df = pd.read_csv(path)  # Reading the CSV file
    return df

# Load the uploaded file
df = load_data(uploaded_file)

# Expandable section to preview the uploaded data
with st.expander("Data Preview"):
    st.dataframe(
        df,  # Displaying the dataframe
        column_config={"User_ID": st.column_config.NumberColumn(format="%d")},  # Formatting User_ID as a number
    )

###################################################################################################

# Creating a gender filter to filter the data based on gender
gender = st.selectbox(
    "Select Gender:",  # Label for the select box
    options=df['Gender'].unique(),  # Extracting unique gender options from the data
    index=1  # Default selection
)

###################################################################################################
# Creating a layout with two columns for the top row of graphs
col1, col2 = st.columns(2)

# Filtering the dataset based on the selected gender
filtered_df = df[df['Gender'] == gender]

##################################################################################################

# Graph 1 (Top Left): Selection for graph type with a radio button
with col1:
    graph_type1 = st.radio(
        "Select Graph Type for Plot1:",
        options=['Average Annual Income vs Profession', 'Average Annual Income vs Health Condition'],  # Graph options
        index=0,  # Default selection
        key='Plot1'
    )
    
    # Plotting the graph based on selected type
    if graph_type1 == 'Average Annual Income vs Profession':
        avg_income_profession = filtered_df.groupby('Professional_Status')['Annual_Income'].mean().reset_index()  # Grouping by profession and calculating mean income
        fig1 = px.bar(avg_income_profession, x='Professional_Status', y='Annual_Income', 
                      title='Average Annual Income vs Profession',
                      color='Professional_Status',  # Adding color by profession
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])  # Custom color palette
    else:
        avg_income_health = filtered_df.groupby('Health_Condition')['Annual_Income'].mean().reset_index()  # Grouping by health condition
        fig1 = px.bar(avg_income_health, x='Health_Condition', y='Annual_Income',
                      title='Average Annual Income vs Health Condition',
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])  # Custom color palette

    # Customizing the layout and colors of the plot
    fig1.update_layout(
        title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20, 'color': '#FFFFFF'}},  # Centering the title
        paper_bgcolor='#4E6E8E',  # Background color
        plot_bgcolor='#4E6E8E',  # Plot background color
        font_color='#FFFFFF',  # Font color
        font_size=14,
        xaxis=dict(showgrid=False),  # Hiding gridlines for x-axis
        yaxis=dict(showgrid=False),  # Hiding gridlines for y-axis
        margin=dict(l=40, r=40, t=40, b=40)  # Adjusting plot margins
    )
    st.plotly_chart(fig1, use_container_width=True)  # Displaying the chart

#######################################################################################################

# Graph 2 (Top Right): Second graph with radio button for type selection
with col2:
    graph_type2 = st.radio(
        "Select Graph Type for Plot2:",
        options=['Average Annual Income vs Membership Type', 'Average Annual Income vs Age'],  # Graph options
        index=0,  # Default selection
        key='Plot2'
    )
    
    # Plotting the graph based on selected type
    if graph_type2 == 'Average Annual Income vs Membership Type':
        avg_income_membership = filtered_df.groupby('Membership_Type')['Annual_Income'].mean().reset_index()  # Grouping by membership type
        fig2 = px.bar(avg_income_membership, x='Membership_Type', y='Annual_Income', 
                      title='Average Annual Income vs Membership Type',
                      color='Membership_Type',  # Adding color by membership type
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])
    else:
        avg_income_age = filtered_df.groupby('Age')['Annual_Income'].mean().reset_index()  # Grouping by age
        fig2 = px.scatter(avg_income_age, x='Age', y='Annual_Income',
                      title='Average Annual Income vs Age',
                      color='Age',  # Adding color by age
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])

    # Customizing the layout and colors of the plot
    fig2.update_layout(
        title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20, 'color': '#FFFFFF'}},  # Centering the title
        paper_bgcolor='#4E6E8E',  # Background color
        plot_bgcolor='#4E6E8E',  # Plot background color
        font_color='#FFFFFF',
        font_size=14,
        xaxis=dict(showgrid=False),  # Hiding gridlines
        yaxis=dict(showgrid=False),
        margin=dict(l=40, r=40, t=40, b=40)  # Adjusting plot margins
    )
    st.plotly_chart(fig2, use_container_width=True)  # Displaying the chart

#####################################################################################################################
# Creating a layout with two columns for the second row of graphs
col3, col4 = st.columns(2)

#####################################################################################################################
# Graph 3 (Bottom Left): Third graph with radio button for type selection
with col3:
    graph_type3 = st.radio(
        "Select Graph Type for Plot3:",
        options=['Average Annual Income vs Location', 'Average Frequency of Visit vs Professional Status'],  # Graph options
        index=0,
        key='Plot3'
    )
    
    if graph_type3 == 'Average Annual Income vs Location':
        avg_income_location = filtered_df.groupby('Location')['Annual_Income'].mean().reset_index()  # Grouping by location
        fig3 = px.bar(avg_income_location, x='Location', y='Annual_Income', 
                      title='Average Annual Income vs Location',
                      color='Location',  # Adding color by location
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])
    else:
        avg_visit_profession = filtered_df.groupby('Professional_Status')['Frequency_of_Visit'].mean().reset_index()  # Grouping by profession
        fig3 = px.bar(avg_visit_profession, x='Professional_Status', y='Frequency_of_Visit',
                      title='Average Frequency of Visit vs Professional Status',
                      color='Professional_Status',  # Adding color by profession
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])

    # Customizing the layout and colors of the plot
    fig3.update_layout(
        title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20, 'color': '#FFFFFF'}},  # Centering the title
        paper_bgcolor='#4E6E8E',  # Background color
        plot_bgcolor='#4E6E8E',  # Plot background color
        font_color='#FFFFFF',
        font_size=14,
        xaxis=dict(showgrid=False),  # Hiding gridlines
        yaxis=dict(showgrid=False),
        margin=dict(l=40, r=40, t=40, b=40)  # Adjusting plot margins
    )
    st.plotly_chart(fig3, use_container_width=True)  # Displaying the chart

####################################################################################################

# Graph 4 (Bottom Right): Fourth graph with radio button for type selection
with col4:
    graph_type4 = st.radio(
        "Select Graph Type for Plot4:",
        options=['Average Annual Income vs Marital Status', 'Average Frequency of Visit vs Preffered Time'],  # Graph options
        index=0,
        key='Plot4'
    )
    
    if graph_type4 == 'Average Annual Income vs Marital Status':
        avg_income_marital = filtered_df.groupby('Marital_Status')['Annual_Income'].mean().reset_index()  # Grouping by marital status
        fig4 = px.bar(avg_income_marital, x='Marital_Status', y='Annual_Income', 
                      title='Average Annual Income vs Marital_Status',
                      color='Marital_Status',  # Adding color by marital status
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])
    else:
        avg_visit_time = filtered_df.groupby('Preferred_Time')['Frequency_of_Visit'].mean().reset_index()  # Grouping by preferred visit time
        fig4 = px.bar(avg_visit_time, x='Preferred_Time', y='Frequency_of_Visit',
                      title='Average Frequency of Visit vs Preferred Time',
                      color='Preferred_Time',  # Adding color by preferred time
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])

    # Customizing the layout and colors of the plot
    fig4.update_layout(
        title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20, 'color': '#FFFFFF'}},  # Centering the title
        paper_bgcolor='#4E6E8E',  # Background color
        plot_bgcolor='#4E6E8E',  # Plot background color
        font_color='#FFFFFF',
        font_size=14,
        xaxis=dict(showgrid=False),  # Hiding gridlines
        yaxis=dict(showgrid=False),
        margin=dict(l=40, r=40, t=40, b=40)  # Adjusting plot margins
    )
    st.plotly_chart(fig4, use_container_width=True)  # Displaying the chart
