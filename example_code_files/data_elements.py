import streamlit as st
import pandas as pd
import seaborn as sns

# using st.dataframe
df = sns.load_dataset('titanic') # loading the titanic dataset from seaborn
st.dataframe(df)

# using st.data_editor()
df = pd.DataFrame({"Task": ["Study", "Code"], "Done": [False, True]})

edited_df = st.data_editor(df, num_rows="dynamic")

st.write("Updated To-Do List:")
st.write(edited_df)

# using st.table()
st.table(df)

# using st.metric()
st.text("Key Metrics")
st.metric(label="Revenue", value="$120K", delta="+8%")

