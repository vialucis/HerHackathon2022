import streamlit as st
from streamlit_chat import message
import pandas as pd
from backend import gpt3_answer

# Sidebar
st.sidebar.title("HerHackathon 2022, Merck Challenge")
def home_page():
    st.markdown("# :mailbox: 🎈")
    st.sidebar.markdown("# :mailbox: 🎈")

def contact():
    st.markdown("# Contact Us ❄️")
    st.sidebar.markdown("# Contact Us ❄️")

def about():
    st.markdown("# About Us 🎉")
    st.sidebar.markdown("# About Us 🎉")


page_names_to_funcs = {
    "Main Page": home_page,
    "Page 2": contact,
    "Page 3": about,
    
   
}
# main part
st.title('Trial Connect')
st.subheader('Helping people find clinical trials')

st.write("Are you struggling to find the best clinical trial suitable for you? We are here to help!")

city = st.selectbox(
    'Which city do you live in?', ["Frankfurt", "Berlin", "Munich"])


message("Hi and welcome to Trial Connect. How can I help you?")
input_text = st.text_area('Your input:', height=100)
bt_send = st.button('Send')
if bt_send:
    output_text = gpt3_answer(input_text)
    message(output_text)