import streamlit as st

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

def render():
    st.title("About Me")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        Hi! I'm **Dhananjay (DJ) Kulkarni**, a Cloud Architecture and Technical Project Manager specializing in AI/ML, Agentic AI, and Next-Gen Contact Centers (CCaaS). I focus on building secure, scalable customer experience systems that leverage the latest in GenAI to drive real-world business impact.
        
        Accomplished Technical Leader and Pre-Sales Architect with 18+ years of experience driving large-scale digital transformations and Data Center Exits for high-compliance enterprises (HIPAA, FedRAMP, GxP). I am an expert in bridging legacy infrastructure with cloud-native innovation, leading C-level stakeholders through modernization strategies to optimize ROI.
        
        I am renowned for revolutionizing Customer Experience (CX) by architecting Agentic AI systems utilizing Model Context Protocol (MCP), Agent-to-Agent (A2A) workflows, and ADKs. I am deeply skilled in integrating Amazon Connect with Generative AI (Bedrock, Lex) to deliver secure, hyper-personalized engagement. As a strategic "trusted advisor", I am adept at aligning technical solutions with Product-Market Fit (PMF) and shaping product roadmaps through expert POC delivery.
        
        **Contact:** dj.kulkarni@gmail.com | Chicago, IL
        """)

            
    with col2:
        st.image("Profile Pic.HEIC", caption="Dhananjay (DJ) Kulkarni", use_container_width=True)
