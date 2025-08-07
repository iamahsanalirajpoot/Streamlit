import streamlit as st
import datetime

st.title("Data and Time input Widget")

# st.date_input
st.subheader("Using st.date_input")

DOB = st.date_input("What's your birthday", datetime.date(2010, 4, 6))
st.write("Your birthday is:", DOB)

# to initialize an empty date input, use None as the value
DOB = st.date_input("What's your birthday", value=None)
st.write("Your birthday is:", DOB)

# st.time_input
st.subheader("Using st.time_input")

alarm = st.time_input("Set an alarm for", value=None)
st.write("Alarm is set for", alarm)