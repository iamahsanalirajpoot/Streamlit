import streamlit as st

st.title("Selection Widgets in Streamlit")

# st.checkbox()
st.subheader("- Using st.checkbox()")

agree = st.checkbox("agree")

if agree:
    st.write("Great!")

# st.color_picker()
st.subheader("- Using st.color_picker()")

color = st.color_picker("Pick A Color")
st.write("The Selected:", color)

# st.feedback()
st.subheader("- Using st.feedback()")

st.feedback("thumbs")
st.feedback("stars")

# st.multiselect()
st.subheader("- Using st.subheader()")

options = st.multiselect(
    "What are your favorite programming language?",
    ["Python", "Cpp", "C", "CSS", "JavaScript"],
    default=["Python"],
    max_selections=3,
    accept_new_options=True
)

# st.pills()
st.subheader("- Using st.pills()")

options = ["Python", "Cpp", "C", "CSS", "JavaScript"]
selection = st.pills("Choose your Favorite Programming Language:", options, selection_mode="single")
st.markdown(f"Your Favorite Programming Language is {selection}")

# st.radio()
st.subheader("- Using st.radio()")

language = st.radio(
    "Select one:",
    ["Python", "JavaScript", "Cpp", "Java"]
)

st.write(f"You selected: **{language}**")

# st.segmented_control()
st.subheader("Using st.segmented_control")

options = ["Python", "Cpp", "C", "CSS", "JavaScript"]
selection = st.segmented_control("Choose your Favorite Programming Language:", options, selection_mode="single")
st.markdown(f"Your Favorite Programming Language is {selection}")

# st.selectbox()
st.subheader("- Using st.selectbox()")

language = st.selectbox(
    "Select one:",
    ["Python", "JavaScript", "Cpp", "Java"]
)

st.write(f"You selected: **{language}**")

# st.toogle()
st.subheader("- Using toogle()")

on = st.toggle("Activate feature")

if on:
    st.write("Feature activated!")
    
