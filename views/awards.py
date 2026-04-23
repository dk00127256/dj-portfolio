import streamlit as st

def render():
    st.title("Awards & Recognition")
    
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("aws-award.JPEG", use_container_width=True)
    with col2:
        st.markdown("### Career Awards & Recognition")
        st.markdown("""
        * 🏆 **AWS GSI Disruptive Architecture Competition 2023**: Awarded first place for innovative solutions.
        * 🎖️ **IBM Excellence Award**: Recognized for managing IVR and CTI infrastructure.
        * 🥇 **Numo Uno (Accenture)**: Achieved for surpassing critical project goals.
        * 👏 **Tech Mahindra**: Honored with a 'Pat on the back' award for exemplary project transition and customer satisfaction.
        """)

