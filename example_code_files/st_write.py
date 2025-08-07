import streamlit as st
import pandas as pd

st.write("Ahsan")

st.write(5238)

# st.write also accepts other data formats
st.write(
    pd.DataFrame(
        {"col1" : [1, 3, 5, 7],
         "col2" : [2, 4, 6, 8]
         }
    )
)