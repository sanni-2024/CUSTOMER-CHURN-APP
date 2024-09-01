import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title= 'View Data',
    page_icon= '',
    layout= 'wide'
)

st.title('DATASETS')
st.write('This page contains  data from an SQL database that was used in this project')


#load data from SQL database
telco_churn_first_3000= pd.read_csv("Datasets/Telco-churn-first-3000")

def display_section(section): 
    if section == "Categorical":
        st.write("Categorical Section:")
        st.write(telco_churn_first_3000.select_dtypes(include=['object']))
    elif section == "Numerical":
        st.write("Numerical Section:")
        st.write(telco_churn_first_3000.select_dtypes(exclude=['object']))



dataset_column, section_column = st.columns([1,1])  

with dataset_column:
    selected_dataset_name = st.selectbox("Select Dataset", ["All Datasets"])

with section_column:
    selected_section = st.selectbox("Select Section", ["Categorical", "Numerical"])        

# Display the selected dataset and section
st.write("Selected Dataset:", selected_dataset_name)
display_section(selected_section)