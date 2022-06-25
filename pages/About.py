import streamlit as st

# Sidebar
st.sidebar.title("HerHackathon 2022")
st.sidebar.subheader("Merck Challenge")

st.header("About Us!")

left_column, right_column = st.columns(2)

left_column.image('images/LucieHuang.jpg', width=200, output_format='JPG')
left_column.subheader("Lucie Huang")
left_column.write("Techie")

right_column.image('images/Shruti.jpg', width=330, output_format='JPG')
right_column.subheader("Shruti")
right_column.write("Techie")