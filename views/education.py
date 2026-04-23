import streamlit as st

def render():
    st.title("Education")
    
    # Degree 1
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("<h1>🎓</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown("### Pune University")
        st.markdown("**B.S.: Electrical, Electronics & Communications Engineering**")
        
    st.markdown("---")
    
    # Degree 2
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown("<h1>📜</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown("### Mumbai University")
        st.markdown("**Diploma: Industrial Electronics**")
