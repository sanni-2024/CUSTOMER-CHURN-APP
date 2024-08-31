
import streamlit as st
import plotly.express as px 
import pandas as pd

st.set_page_config(
    page_title='Dashboard',
    page_icon='',
    layout='wide'
)

st.title('Dashboard')
st.markdown('This page provides insights on the factors that may lead to customer churn')

# Load the data using pandas
Cleaned_dataset = pd.read_csv("Datasets/Cleaned_dataset")


selectbox_column, visualization_column = st.columns([1, 4])
visualization_category = selectbox_column.selectbox(
    "Select Visualization Category",
    ["KPI", "Univariate Analysis"]
)

# Churn rate among senior citizens
senior_citizen = Cleaned_dataset[Cleaned_dataset['SeniorCitizen'] == 'Yes']
churn_senior = senior_citizen['Churn'].value_counts(normalize=True) * 100
churn_senior = churn_senior.reset_index()

# Payment method with the highest churn rate
payment_churn = Cleaned_dataset.groupby('PaymentMethod')['Churn'].value_counts(normalize=True).unstack()
churn_rate = payment_churn['Yes']

# Churn rate by Internet Service
internet_churn_group = Cleaned_dataset.groupby('InternetService')['Churn'].value_counts(normalize=True)
fiber_optic_churn_rate = round(internet_churn_group.loc['Fiber optic', 'Yes'] * 100, 2)
dsl_churn_rate = round(internet_churn_group.loc['DSL', 'Yes'] * 100, 2)

# Churn rate by Contract duration
contract_churn_rate = Cleaned_dataset.groupby('Contract')['Churn'].value_counts().unstack()

# Convert monthly charges and total charges columns to numeric
Cleaned_dataset['MonthlyCharges'] = pd.to_numeric(Cleaned_dataset['MonthlyCharges'], errors='coerce')
Cleaned_dataset['TotalCharges'] = pd.to_numeric(Cleaned_dataset['TotalCharges'], errors='coerce')

numerical_columns = ['TotalCharges', 'MonthlyCharges','Tenure']
numerical_data = Cleaned_dataset[numerical_columns]

# Add columns to the dashboard page
col1, col2 = st.columns(2)

if visualization_category == "KPI":
    with col1:
        fig1 = px.bar(churn_senior, x='Churn', y='proportion', color='Churn',
                      labels={'proportion': 'Percentage (%)', 'Churn': 'Churn'},
                      title='Churn Rate Among Senior Citizens')
        st.plotly_chart(fig1, use_container_width=True)

        fig2 = px.pie(names=churn_rate.index, values=churn_rate.values,
                      title='Churn Rate by Payment Method',
                      labels={'names': 'Payment Method', 'values': 'Churn Rate (%)'})
        fig2.update_layout(height=400, width=400)  # Adjust height and width
        st.plotly_chart(fig2, use_container_width=True)


with col2:
        fig4 = px.bar(contract_churn_rate, x=contract_churn_rate.index, y='Yes',
                      labels={'x': 'Contract Duration', 'y': 'Churn Count'},
                      title='Churn Rate by Contract Duration')
        st.plotly_chart(fig4, use_container_width=True)
        
        fig3 = px.bar(x=['Fiber optic', 'DSL'], y=[fiber_optic_churn_rate, dsl_churn_rate],
                      text=[f'{fiber_optic_churn_rate}%', f'{dsl_churn_rate}%'],
                      labels={'x': 'Internet Service', 'y': 'Churn Rate'},
                      title='Churn Rate by Internet Service')
        st.plotly_chart(fig3, use_container_width=True)  
        
with col1:
        fig5 = px.histogram(Cleaned_dataset, x='TotalCharges', nbins=20, title="Histogram of Tenure")
        st.plotly_chart(fig5, use_container_width=True)

with col2:
        fig6 = px.histogram(Cleaned_dataset, x='MonthlyCharges', nbins=20, title="Histogram of Monthly Charges")
        st.plotly_chart(fig6, use_container_width=True)
        
        fig7 = px.histogram(Cleaned_dataset, x='Tenure', nbins=20, title="Histogram of Tenure")
        st.plotly_chart(fig7, use_container_width=True)
         

