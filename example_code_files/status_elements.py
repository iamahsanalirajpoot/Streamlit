import streamlit as st
import time

st.title("Status Elements")

# st.status()
st.success("Successfull!", icon="✅")

# st.status()
with st.status("Downloading data..."):
    st.write("Searching for data...")
    time.sleep(1)
    st.write("Found URL.")
    time.sleep(0.5)
    st.write("Downloading data...")
    time.sleep(0.5)

# st.info()
st.info('make sure you use secure password!', icon="ℹ️")

# st.warning()
st.warning("Sensetive data", icon="⚠️")

# st.spinner()
with st.spinner("Wait for it...", show_time=True):
    time.sleep(5)
st.success("Done!")

# st.error()
st.error("Error")

# st.balloons()
st.balloons()

# st.snow()
st.snow()