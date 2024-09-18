#Importing all the libraries
import plotly.express as px
import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib as plt
import seaborn as sns

####################################################################################################

#Creation of the Dashboard
st.set_page_config(page_title="Income Distribution Dashboard", page_icon=":bar_chart:", layout="wide")

st.title("Income Distribution Dashboard")

st.markdown("Data Science Group 2")

with st.sidebar:
    st.header("Configuration")
    uploaded_file = st.file_uploader("Choose a file")
        # Adding a toggle switch for light/dark mode
if uploaded_file is None:
    st.info(" Upload a file through config", icon="ℹ️")
    st.stop()


###################################################################################################

#Storing data

@st.cache_data
def load_data(path: str):
    df = pd.read_csv(path)
    return df


df = load_data(uploaded_file)

with st.expander("Data Preview"):
    st.dataframe(
        df,
        column_config={"User_ID": st.column_config.NumberColumn(format="%d")},
    )

###################################################################################################

#Creation of the Gender Filter Above the Graphs


#Gender Filter
gender = st.selectbox(
    "Select Gender:",
    options=df['Gender'].unique(),
    index=1
)


###################################################################################################
#layout for two columns on the top row 
col1, col2 = st.columns(2)

#filter the dataframe based on the selected gender
filtered_df = df[df['Gender'] == gender]

##################################################################################################

#Graph 1(TOP LEFT)
with col1:
    graph_type1 = st.radio(
        "Select Graph Type for Plot1:",
        options=['Average Annual Income vs Profession', 'Average Annual Income vs Health Condition'],
        index=0,
        key='Plot1'
    )
    
    if graph_type1 == 'Average Annual Income vs Profession':
        #Group by Professional Status mean of Annual Income
        avg_income_profession = filtered_df.groupby('Professional_Status')['Annual_Income'].mean().reset_index()
        fig1 = px.bar(avg_income_profession, x='Professional_Status', y='Annual_Income', 
                      title='Average Annual Income vs Profession',
                      color='Professional_Status',
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])
    else:
        #group by Health Condition and mean of Annual Income
        avg_income_health = filtered_df.groupby('Health_Condition')['Annual_Income'].mean().reset_index()
        fig1 = px.bar(avg_income_health, x='Health_Condition', y='Annual_Income',
                      title='Average Annual Income vs Health Condition',
                
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])

    fig1.update_layout(
        title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20, 'color': '#FFFFFF'}},
        paper_bgcolor='white',
        plot_bgcolor='white',
        font_color='black',
        font_size=14,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig1, use_container_width=True)

#######################################################################################################

#Graph 2(Top Right)

with col2:
    graph_type2 = st.radio(
        "Select Graph Type for Plot2:",
        options=['Average Annual Income vs Age', 'Average Annual Income vs Membership Type'],
        index=0,
        key='Plot2'
    )
    
    if graph_type2 == 'Average Annual Income vs Age':
        #Group by age and annual income mean
        avg_income_age = filtered_df.groupby('Age')['Annual_Income'].mean().reset_index()
        fig2 = px.scatter(avg_income_age, x='Age', y='Annual_Income',
                      title='Average Annual Income vs Age',
                      color='Age',
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])
    else:
        #group by Membership Type and annual income mean
        avg_income_membership = filtered_df.groupby('Membership_Type')['Annual_Income'].mean().reset_index()
        fig2 = px.bar(avg_income_membership, x='Membership_Type', y='Annual_Income', 
                      title='Average Annual Income vs Membership Type',
                      color='Membership_Type',
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])

    fig2.update_layout(
        title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20, 'color': '#FFFFFF'}},
        paper_bgcolor='white',
        plot_bgcolor='white',
        font_color='black',
        font_size=14,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig2, use_container_width=True)






#####################################################################################################################
#Layout for two columns on the top row 
col3, col4 = st.columns(2)

#####################################################################################################################
#graph 3(bottom left)

with col3:
    graph_type3 = st.radio(
        "Select Graph Type for Plot3:",
        options=['Average Annual Income vs Location', 'Average Annual Income vs Marital Status'],
        index=0,
        key='Plot3'
    )
    
    if graph_type3 == 'Average Annual Income vs Location':
        #grouped by Professional Status and annual income mean
        avg_income_location = filtered_df.groupby('Location')['Annual_Income'].mean().reset_index()
        fig3 = px.bar(avg_income_location, x='Annual_Income', y='Location', 
                      title='Average Annual Income vs Location',
                      color='Location',
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'],
                      orientation="h")

    else:
        #group by professional Status and annual income mean
        avg_income_marital = filtered_df.groupby('Marital_Status')['Annual_Income'].mean().reset_index()
        fig3 = px.bar(avg_income_marital, x='Annual_Income', y='Marital_Status', 
                      title='Average Annual Income vs Marital_Status',
                      color='Marital_Status',
                      color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'],
                      orientation="h")

    fig3.update_layout(
        title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20, 'color': '#FFFFFF'}},
        paper_bgcolor='white',
        plot_bgcolor='white',
        font_color='black',
        font_size=14,
        height=500,  
        margin=dict(l=60, r=40, t=40, b=40), 
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
            )
    st.plotly_chart(fig3, use_container_width=True)

############################################################################################
#graph 4(Bottom Right)
with col4:
    graph_type4 = st.radio(
        "Select Graph Type for Plot4:",
        options=['Average Frequency of Visit vs Professional Status', 'Average Frequency of Visit vs Preffered Time'],
        index=0,
        key='Plot4'
    )
    
    if graph_type4 == 'Average Frequency of Visit vs Professional Status':
        #group by Professional Status and mean frequency of visit
        avg_visit_profession = filtered_df.groupby('Professional_Status')['Frequency_of_Visit'].mean().reset_index()
        fig4 = px.pie(avg_visit_profession, values="Frequency_of_Visit", names="Professional_Status", title="Average Frequency of Visit vs Professional Status")
    else:
        #group by Professional Status and mean Frequency of Visit
        avg_visit_time = filtered_df.groupby('Preferred_Time')['Frequency_of_Visit'].mean().reset_index()
        fig4 = px.pie(avg_visit_time, values="Frequency_of_Visit", names="Preferred_Time")

    fig4.update_layout(
        title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20, 'color': '#FFFFFF'}},
        paper_bgcolor='white',
        plot_bgcolor='white',
        font_color='black',
        font_size=14,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        margin=dict(l=40, r=40, t=40, b=40)
    )
    st.plotly_chart(fig4, use_container_width=True)