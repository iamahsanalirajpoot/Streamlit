import streamlit as st

st.title("Form in Streamlit")

with st.form("user_info"):
    name = st.text_input("Enter your name:")
    age = st.number_input("Your age", min_value=0, max_value=100)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.success(f"Welcome {name}! you are {age} years old.")