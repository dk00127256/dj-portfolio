import streamlit as st

def render():
    st.title("Contact Me")
    st.markdown("Feel free to reach out to me for any inquiries or collaborations!")
    
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submitted = st.form_submit_button("Send")
        if submitted:
            st.success("Message sent! (This is a mock form)")
