import streamlit as st

st.title("Numeric Input Widget")

# st.number_input()
st.subheader("Using st.number_input")

number = st.number_input("Insert a number")
st.write("The number you insert is :", number)

# To initialize an empty number input, use None as the value:
number2 = st.number_input(
    "Insert a number", value=None, placeholder="Type a number..."
)
st.write("The number you insert is :", number2)

# st.slider()
st.subheader("Using st.slider()")

age = st.slider("How old are you?", 0, 120, 18)
st.write("I'm ", age, "years old")

# range slider
values = st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)