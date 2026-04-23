import streamlit as st

def render():
    st.title("Experience")
    
    st.markdown("### Pre-Sales Architect & Technical Leader @ AWS (Amazon Web Services)")
    st.markdown("**18+ Years of Experience**")
    st.markdown("""
    * Driven large-scale digital transformations and Data Center Exits for high-compliance enterprises (HIPAA, FedRAMP, GxP).
    * Led C-level stakeholders through MPA/CAF assessments and 7R modernization strategies to optimize ROI.
    * Revolutionized Customer Experience (CX) by architecting Agentic AI systems utilizing Model Context Protocol (MCP), Agent-to-Agent (A2A) workflows, and ADKs.
    * Integrated Amazon Connect with Generative AI (Bedrock, Lex) to deliver secure, hyper-personalized engagement.
    * Aligned technical solutions with Product-Market Fit (PMF) and shaped product roadmaps through expert POC delivery.
    """)
    skills = ["Amazon Connect", "Generative AI", "AWS Bedrock", "Agentic AI", "Pre-Sales", "Cloud Architecture"]
    tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
    st.markdown(tags, unsafe_allow_html=True)
