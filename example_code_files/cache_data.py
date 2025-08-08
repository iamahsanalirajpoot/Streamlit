import streamlit as st
import time

# Function to simulate slow data loading
@st.cache_data
def load_data():
    time.sleep(3)  # Simulate a slow process
    return {"name": "Ahsan", "age": 18}

st.title("st.cache_data() Demo")

if st.button("Load Data"):
    data = load_data()
    st.write("Data loaded:", data)
    st.button("Rerun")