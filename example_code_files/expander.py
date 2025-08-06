import streamlit as st

st.title("Expander in Streamlit")
st.subheader("Use expander function to hide or show content")

with st.expander("Click here"):
    st.write("keep going...One day, you will make it!")