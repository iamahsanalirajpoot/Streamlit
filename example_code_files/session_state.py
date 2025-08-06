import streamlit as st

st.title("Session State in Streamlit")

if "count" not in st.session_state:
    st.session_state.count = 0


if st.button("Click Me"):
    st.session_state.count += 1

st.write(f"Button clicked: {st.session_state.count} times")