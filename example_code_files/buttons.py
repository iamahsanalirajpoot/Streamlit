import streamlit as st

st.title("Buttons In Streamlit")

# st.button()
st.text("- Using st.button()")

if st.button("Say hello"):
    st.write("Hello, Ahsan! :sunglasses:")

left, middle, right = st.columns(3)

if left.button("Plain Button"):
    left.markdown("You clicked the plain button.")
if middle.button("Emoji Button", icon="😎"):
    middle.markdown("You clicked the emoji button.")
if right.button("Material button", icon=":material/mood:"):
    right.markdown("You clicked the Material button.")

# st.form_submit_button()
st.text("- Using st.form_submit_button()")

with st.form("my_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age")
    submit = st.form_submit_button("Submit")

if submit:
    st.success(f"Hello {name}, you are {int(age)} years old!")

# st.link_button()
st.text("- Using st.link_button()")

st.link_button("My GitHub", "https://github.com/iamahsanalirajpoot")