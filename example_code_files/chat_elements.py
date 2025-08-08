import streamlit as st

st.subheader("Chat Elements")

# st.chat_input()
st.subheader("Using st.chat_input")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")

# st.chat_message()
with st.chat_message("user"):
    st.write("Hello 👋")

message = st.chat_message("assistant")
message.write("Hello human")

# st.status()