import streamlit as st

# Sidebar
st.sidebar.image('images/Trial_Connect_Logo_Logo.png', width=200, output_format='PNG')
st.sidebar.title("HerHackathon 2022")
st.sidebar.subheader("Merck Challenge")

st.header("About us!")

left_column, right_column = st.columns(2)

image_width = 200

left_column.image('images/Lucie.jpg', width=image_width, output_format='JPG')
left_column.subheader("Lucie Huang")
left_column.write("Technical prototype")

right_column.image('images/Shruti.jpg', width=image_width, output_format='JPG')
right_column.subheader("Shruti Pistolwala")
right_column.write("Technical prototype")

left_column.image('images/Rachael.jpeg', width=image_width, output_format='JPEG')
left_column.subheader("Rachael Camp")
left_column.write("UX/UI design")

right_column.image('images/Leticia.JPG', width=image_width, output_format='JPG')
right_column.subheader("Letícia Gonçalves dos Santos")
right_column.write("UX/UI design")

left_column.image('images/Anran.jpg', width=image_width, output_format='JPG')
left_column.subheader("Anran Cai")
left_column.write("Business model")

right_column.image('images/Arati.jpg', width=image_width, output_format='JPG')
right_column.subheader("Arati Shinde")
right_column.write("Business model")