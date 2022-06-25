import streamlit as st

# Sidebar
st.sidebar.image('images/Trial_Connect_Logo_Logo.png', width=200, output_format='PNG')
st.sidebar.title("HerHackathon 2022")
st.sidebar.subheader("Merck Challenge")

st.header(":mailbox: Get in touch with us!")

contact_form="""

<form method="POST" action="https://formsubmit.co/lucie.huang314@gmail.com" enctype="multipart/form-data">
    <input type="email" name="email" placeholder="Your email"><br><br>
    <textarea name="message" placeholder="Your text"></textarea><br><br>
    <input type="file" name="attachment" accept="image/png, image/jpeg"><br><br>
    <button type="submit">Send</button>
</form>

"""

st.markdown(contact_form, unsafe_allow_html=True)