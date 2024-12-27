import streamlit as st
import pandas as pd
import pickle


with open("car_price_model.pkl", "rb") as file:
    model = pickle.load(file)


st.set_page_config(
    page_title="Ford Car Price Prediction App",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar for input fields
st.sidebar.header("Car Details")
model_options = ["Fiesta", "Focus", "Mondeo", "Kuga", "EcoSport"]
model_input = st.sidebar.selectbox("Model", model_options)
year_input = st.sidebar.slider("Year of Manufacture", min_value=2000, max_value=2024, value=2010, step=1)
transmission_input = st.sidebar.selectbox("Transmission", ["Manual", "Automatic", "Semi-Auto"])
mileage_input = st.sidebar.slider("Mileage (in miles)", min_value=0, max_value=300000, value=50000, step=1000)
fuel_type_input = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel", "Hybrid", "Electric"])
tax_input = st.sidebar.number_input("Road Tax", min_value=0, step=10)
mpg_input = st.sidebar.slider("Miles Per Gallon (MPG)", min_value=0.0, max_value=100.0, value=30.0, step=0.1)
engine_size_input = st.sidebar.number_input("Engine Size (in liters)", min_value=0.0, step=0.1)

# Main content layout
st.title("Ford Car Price Prediction App")
st.markdown(
    """<style>
    .main { background-color: #1E1E1E; color: white; font-family: Arial, sans-serif; }
    .css-18e3th9 { background-color: #121212 !important; }
    .stButton>button { background-color: #FF4B4B; color: white; border-radius: 5px; border: none; padding: 10px 20px; }
    </style>""",
    unsafe_allow_html=True
)

st.write("Welcome to the **Ford Car Price Prediction App**! This application predicts the price of a car based on various input features. Use the form on the sidebar to input car details and get a prediction.")

# Predict button
if st.button("Predict Price"):
    # Create a dataframe for the input
    input_data = pd.DataFrame({
        'model': [model_input],
        'year': [year_input],
        'transmission': [transmission_input],
        'mileage': [mileage_input],
        'fuelType': [fuel_type_input],
        'tax': [tax_input],
        'mpg': [mpg_input],
        'engineSize': [engine_size_input]
    })

    # Make prediction
    prediction = model.predict(input_data)
    st.success(f"The predicted price of the car is: \u00a3{prediction[0]:,.2f}")

# Footer
st.markdown(
    """---
    Developed by Ishara Madusanka
    """
)
