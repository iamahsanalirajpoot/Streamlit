import streamlit as st

st.title("Layouts and Containers in Streamlit")
# st.columns()
st.subheader("Using st.columns()")

col1, col2 = st.columns(2)

with col1:
    st.header("Cat")
    st.image("https://shorturl.at/lVZVw")

with col2:
    st.header("Zebra")
    st.image("https://shorturl.at/tWDGu")

left, middle, right = st.columns(3, vertical_alignment="bottom")

left.text_input("Write something")
middle.button("Click me", use_container_width=True)
right.checkbox("Check me")

# st.container()
st.subheader("Using st.container")

container = st.container(border=True)
container.write("This is inside the container")
st.write("This is outside the container")

container.write("This is inside too")

# st.tab()
st.subheader("Using st.tab")

tab1, tab2 = st.tabs(["Cat", "Zebra"])

with tab1:
    st.header("Cat")
    st.image("https://shorturl.at/lVZVw")

with tab2:
    st.header("Zebra")
    st.image("https://shorturl.at/tWDGu")