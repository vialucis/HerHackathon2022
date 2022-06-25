import streamlit as st
# Sidebar
st.sidebar.title("HerHackathon 2022, Merck Challenge")
st.header(":mailbox: Get in Touch with me!")

contact_form="""

<form method="POST" action="https://formsubmit.co/pistolwalashruti@gmail.com" enctype="multipart/form-data">
    <input type="email" name="email" placeholder="Your email"><br><br>
    <textarea name="message" placeholder="Details of your problem"></textarea><br><br>
    <input type="file" name="attachment" accept="image/png, image/jpeg"><br><br>
    <button type="submit">Send Test</button>
</form>

"""

st.markdown(contact_form, unsafe_allow_html=True)