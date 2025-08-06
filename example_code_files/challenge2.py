import streamlit as st
import pandas as pd
import numpy as np

# Initializing session state for chart count
if "chart_count" not in st.session_state:
    st.session_state.chart_count = 0

st.title("Data Visualizer App")
st.write("Select chart type to visualize random data.")

# Form for input selection
with st.form("chart_form"):
    chart_type = st.selectbox("Choose chart type", ["Line Chart", "Bar Chart", "Area Chart"])
    rows = st.slider("Select number of data rows", min_value=5, max_value=100, value=20)
    columns = st.slider("Select number of columns", min_value=1, max_value=5, value=2)
    submit = st.form_submit_button("Generate Chart")

if submit:
    # generating random df
    data = pd.DataFrame(np.random.randn(rows, columns), columns=[f"Col {i+1}" for i in range(columns)])

    # displaying the selected chart
    st.success(f"Showing {chart_type} with {rows} rows and {columns} columns")

    if chart_type == "Line Chart":
        st.line_chart(data)
    elif chart_type == "Bar Chart":
        st.bar_chart(data)
    elif chart_type == "Area Chart":
        st.area_chart(data)

    # counting chart generations
    st.session_state.chart_count += 1

    st.info(f"You have generated {st.session_state.chart_count} charts during this session.")

# Expand to see raw data
with st.expander("View Raw Data"):
    if submit:
        st.dataframe(data)
    else:
        st.write("Submit the form to see data.")
