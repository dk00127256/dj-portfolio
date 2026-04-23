import streamlit as st
import os

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

def render():
    st.title("Volunteering")
    st.markdown("### Moments in Action")
    
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.image("Volunteering2.HEIC", caption="Volunteering", use_container_width=True)
        st.image("Volunteering5.HEIC", caption="Community Work", use_container_width=True)
        
    with c2:
        st.image("Volunteering3.HEIC", caption="Teaching", use_container_width=True)
        st.image("Voluneerting6.HEIC", caption="Event Support", use_container_width=True)
        
    with c3:
        st.image("Volunteering1.HEIC", caption="Community Engagement", use_container_width=True)
        st.image("Volunteering4.JPEG", caption="Making a Difference", use_container_width=True)
