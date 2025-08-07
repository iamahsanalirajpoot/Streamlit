import streamlit as st

st.title("Formatted Text in Streamlit")

# st.badge()
st.badge("New")
st.badge("success", icon=":material/check:", color="green")
st.markdown(
    ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
)

# st.caption()
st.caption("caption")
st.caption("**Note:** You can only upload `.csv` files.")
st.caption("_Caption_ :blue[colors] emojis :sunglasses:")

# st.code()
code = '''print("Ahsan Rajpoot")'''
st.code(code, language="python")

# st.divider()
st.divider()  # draw a horizontal line 

# st.echo()
with st.echo(): # Show and Run Code
   a = 10
   b = 20
   st.write(a + b)

# st.latex()
st.latex(r'''
    (a + b)^2 = a^2 + b^2 + 2ab
    ''')

# st.text()
st.text("My self Ahsan, and I love doing coding!")


