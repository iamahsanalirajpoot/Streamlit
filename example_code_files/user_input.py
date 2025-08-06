import streamlit as st

st.title("Streamlit User Input Widgets")
st.header("Common user input Widgets")

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=100)
date_of_birth = st.date_input("Select your birth date")
rating = st.slider("Give Feedback:", 1, 5)
gender = st.radio("Select gender", ["Male", "Female", "Other"])
hobbies = st.multiselect("Select hobbies", ["Reading", "Coding", "Video Games", "Running", "Hiking", "Cricket"])
agree = st.checkbox("I agree to term and conditions")

if st.button("Submit"):
    st.write(f"Name : {name}, Age : {age}, Date of Birth : {date_of_birth}, Gender : {gender}")
    st.write(f"Hobbies : {', '.join(hobbies)}")
    st.write("Agreement:", "Accepted" if agree else "Not Accepted")