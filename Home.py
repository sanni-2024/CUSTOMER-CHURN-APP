import streamlit as st
import joblib

# Create a function to authenticate users
def authenticate(username, password):

  if username == "Sanni" and  password == "minded123":
      
      return True
  else:
        
        return False

import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":)",
    layout="wide",  # Options are "centered" or "wide"
    initial_sidebar_state="expanded",  # Options are "expanded" or "collapsed"
     )
def main():
 st.title("Customer Churn Prediction App")
 st.subheader("Login Credentials")
 st.markdown(
        """
        * **User_Name:** Sanni
        * **Password:** minded123. 
        """
    )
# Create input fields for username and password
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

# Check if the user has submitted the login form
if st.sidebar.button("Login"):
        if authenticate(username, password):
            st.success("Logged in as {}".format(username))
            # Once authenticated, show the rest of the app            
            
        def show_app():
             print("This is the start of the function.")
             print("This line is correctly indented.")
else:
            
        st.error("Invalid username or password")

# Define the rest of the app to show after authentication
def show_app():
    st.subheader("About App:")
    st.markdown(
          """_The Vodafone Customer Churn Mitigation Project is an ambitious initiative aimed at understanding, analyzing, and ultimately reducing customer attrition within our telecommunications services.
         This app aims at using  machine learning models that will predict the likelihood of a customer churning._"""
      )
st.subheader("Key Features:")
st.markdown(
        """
        * **Data_page:** _Contains all the datasets that was used in analyzing and training machine learning models._
        * **Dashboard:** _This page contains all the visuals that were created during our analysis._
        * **Predict_page:** _This page allows you to predict the likelyhood of a customer churning._
        * **History_page:** _The predict page serves as an archive for all predictions that were done in the predict page._
        """
    )
st.subheader("Contact Details:")
st.markdown(
        """
        * **📧Email:** sannyssif23@gmail.com.
        * **🐱‍👤Github:** https://github.com/sanni-2024.
        """
    
    )

st.markdown('professionalism is the field of an excellent person'
    
)

# Check if the script is being run directly
if __name__ == "__main__":
    main()  


