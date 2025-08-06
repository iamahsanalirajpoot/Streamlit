# 4. Adds an expandable section with a short bio about yourself.

import streamlit as st

st.title("Challenge 1")
st.subheader("Create a small app that:")
st.text("""1. Takes name, age, and favorite programming language.
2. Shows an image or video.
3. Uses a button to display all input values in a friendly format.
4. Adds an expandable section with a short bio about yourself.""")

# taking name, age and favourite programming language
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=0, max_value=100)
fav_language = st.radio("Choose your favorite programming language",["Python", "C", "C++", "JavaScript", "CSS", "SQL", "R"])

# showing image and video
st.image("https://shorturl.at/paluU", caption="Profile Picture")
st.video("https://www.youtube.com/watch?v=yKTEC1Y5bEQ")

# displaying input 
if st.button("View your details"):
    st.write(f"Your name is {name}")
    st.write(f"You are {age} year old")
    st.write(f"Your favorite programing language is {fav_language}")

# creating expandable section for short bio
with st.expander("See my bio"):
    st.markdown("""
    **Ahsan Rajpoot** ICS Student 
    Learning Python, AI, ML And Deep Learning
    Feature AI Engineer""")

