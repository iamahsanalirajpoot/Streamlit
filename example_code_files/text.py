import streamlit as st

st.title("Text Wedget in Streamlit")

# st.text_input()
st.subheader("Using st.text_input")

text = st.text_input("What is your Name?")
st.write("Your name is", text)

# st.text_area()
st.subheader("Using st.text_input")

txt = st.text_area("Insert a paragraph for finding out the lenght:")

submit = st.button("submit")

if submit:
    st.write(f"you wrote {len(txt)} characters.")

# st.chat_input()
st.subheader("Using st.chat_input")

prompt = st.chat_input("Say something...")

if prompt:
    st.write(f"User has sent the prompt: {prompt}")