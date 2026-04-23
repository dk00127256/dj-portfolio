import streamlit as st
import os

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

def render():
    st.title("Photo Gallery")
    st.markdown("A collection of moments from various speaking engagements and events.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.image("Reinvent 2024.HEIC", caption="Re:Invent 2024")
        st.image("Reinvent 2024 booth.HEIC", caption="Re:Invent 2024 Booth")
        st.image("TechSummit 2024.JPEG", caption="TechSummit 2024")
        
    with col2:
        st.image("Reinvent 2024 with Jeff Barr.HEIC", caption="With Jeff Barr")
        st.image("Reinvent 2025 Session.HEIC", caption="Re:Invent 2025 Session")
        st.image("Training.JPEG", caption="Training Session")
        
    with col3:
        st.image("Reinvent 2025 booth.HEIC", caption="Re:Invent 2025 Booth")
