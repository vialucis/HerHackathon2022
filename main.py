import streamlit as st
from streamlit_chat import message
import pandas as pd
from backend import test_gpt3_integration

# main part
st.title('Clinical Wise')
st.subheader('Helping people find clinical trials')

st.write("Lorem Ipsum")

input_text = st.text_area('Paste your text here:', height=200)

language_choices = pd.DataFrame({
    'languages': ["German", "English"]
})

language = st.selectbox(
    'Which language do you prefer?', language_choices['languages'])

bt_gpt3 = st.button('GPT-3')

if bt_gpt3:
    output_text = test_gpt3_integration(input_text)

    st.write("__Output text:__")
    st.write(output_text)

message("My message")
message("Hello bot!", is_user=True)

# Sidebar
st.sidebar.header("HerHackathon 2022")