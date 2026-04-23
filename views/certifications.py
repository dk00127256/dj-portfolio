import streamlit as st

def render():
    st.title("Certifications & Badges")
    
    st.markdown("### Amazon Web Services (AWS)")
    aws_certs = [
        "AWS Certified Solutions Architect – Associate",
        "AWS Certified Cloud Practitioner – Foundational",
        "AWS Certified AI Practitioner – Foundational",
        "AWS Generative AI Accreditation – Foundational",
        "AWS Cloud Economics Accredited Partner",
        "Technical Accredited Partner",
        "AWS Well-Architected Proficient"
    ]
    for cert in aws_certs:
        st.markdown(f"- ☁️ **{cert}**")
        
    st.markdown("---")
    st.markdown("### Amazon Connect Specialist Badges")
    connect_certs = [
        "Amazon Connect Developer",
        "Amazon Connect Fundamentals",
        "Amazon Connect AI Fundamentals",
        "Amazon Connect Communications Specialist",
        "Amazon Connect Reporting & Analytics"
    ]
    for cert in connect_certs:
        st.markdown(f"- 🎧 **{cert}** (Trained)")

    st.markdown("---")
    st.markdown("### Google Cloud")
    gcp_certs = [
        "Introduction to Responsible AI",
        "Introduction to Large Language Models",
        "Introduction to Generative AI",
        "Applying AI Principles with Google Cloud",
        "Generative AI Fundamentals"
    ]
    for cert in gcp_certs:
        st.markdown(f"- 🌐 **{cert}**")
