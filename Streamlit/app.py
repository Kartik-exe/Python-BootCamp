import streamlit as st
import pandas as pd
import numpy as np

## Title of the Application
st.title("It's Kartik's application!")

## Display a Simple Text
st.write("It's a Text!")


#Creating a dataFrame!

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10, 20, 30, 40]
})


## Display the DataFrame
st.write("Here's my DataFrame")
st.write(df)


## Create a line chart

chart_data=pd.DataFrame(
    np.random.randn(20,3), columns = ['a', 'b', 'c']
)
st.line_chart(chart_data)