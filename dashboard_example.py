import dash
import plotly.express as px
import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('gym_membership_prediction_with_professional_status.csv')

st.set_page_config(page_title="Income Distribution Dashboard", layout="centered")

st.title("Income Distribution Dashboard")

gender = st.selectbox(
    "Select Gender:",
    options=df['Gender'].unique(),
    index=1
)

graph_type = st.radio(
    "Select Graph Type:",
    options=['Annual Income vs Profession', 'Annual Income vs Age'],
    index=0
)

filtered_df = df[df['Gender'] == gender]

if graph_type == 'Annual Income vs Profession':
    fig = px.bar(filtered_df, x='Professional', y='Annual Income', 
                 title='Annual Income vs Profession', 
                 color='Professional', 
                 color_discrete_sequence=['#FF5733', '#FFC300', '#DAF7A6'])
else:
    fig = px.scatter(filtered_df, x='Age', y='Annual Income', 
                     title='Annual Income vs Age', 
                     color='Age', 
                     color_continuous_scale=px.colors.sequential.Viridis)

fig.update_layout(
    title={'x': 0.5, 'xanchor': 'center', 'font': {'size': 20, 'color': '#FFFFFF'}},
    paper_bgcolor='#4E6E8E',
    plot_bgcolor='#4E6E8E',
    font_color='#FFFFFF',
    font_size=14,
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    margin=dict(l=40, r=40, t=40, b=40)
)

st.plotly_chart(fig, use_container_width=True)