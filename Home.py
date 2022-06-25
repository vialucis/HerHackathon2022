import streamlit as st
from streamlit_chat import message
import pandas as pd
from backend import gpt3_answer
import translators as ts

# Sidebar
st.sidebar.image('images/Trial_Connect_Logo_Logo.png', width=200, output_format='PNG')
st.sidebar.title("HerHackathon 2022")
st.sidebar.subheader("Merck Challenge")

def home_page():
    st.markdown("# :mailbox: 🎈")
    st.sidebar.markdown("# :mailbox: 🎈")

def contact():
    st.markdown("# Contact Us ❄️")
    st.sidebar.markdown("# Contact Us ❄️")

def about():
    st.markdown("# About Us 🎉")
    st.sidebar.markdown("# About Us 🎉")

# main part
st.image('images/Trial_Connect_Logo_Logo.png', width=200, output_format='PNG')
st.title('Trial Connect')
st.subheader('Helping people find clinical trials')

st.write("Are you struggling to find the best clinical trial suitable for you? We are here to help!")

language = st.selectbox(
    'Which language do you prefer?', ["English", "German", "Turkish", "Arabic", "Chinese", "Spanish"])

language_code_dict = {
    "English": "en",
    "German": "de",
    "Turkish": "tr",
    "Arabic": "ar",
    "Chinese": "zh",
    "Spanish": "es"
}

language_code = language_code_dict[language]

audio_flag = st.checkbox('Audio assistance')

message(ts.google("Hi and welcome to Trial Connect. How can I help you?", from_language='en', to_language=language_code))

input_text = st.text_area(ts.google("Your input:", from_language='en', to_language=language_code), height=100)
bt_send = st.button(ts.google("Send", from_language='en', to_language=language_code))
if bt_send:
    input_text_en = ts.google(input_text, from_language=language_code, to_language='en')
    output_text_en = gpt3_answer(input_text_en)
    output_text = ts.google(output_text_en, from_language='en', to_language=language_code)
    message(output_text)
