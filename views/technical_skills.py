import streamlit as st

def render():
    st.title("Technical Skills")
    
    st.markdown("### Agentic AI & ML Ecosystem")
    ai_skills = ["Agent-to-Agent (A2A) Orchestration", "Model Context Protocol (MCP)", "OpenClaw", "Agent Development Kits (ADK)"]
    tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in ai_skills])
    st.markdown(tags, unsafe_allow_html=True)
    
    st.markdown("### Generative AI")
    gen_ai = ["Retrieval-Augmented Generation (RAG)", "Amazon Bedrock", "Lex", "SageMaker", "Agents for Amazon Bedrock", "AWS Strands Agents SDK"]
    tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in gen_ai])
    st.markdown(tags, unsafe_allow_html=True)
    
    st.markdown("### Advanced ML & Technologies")
    ml_skills = ["Prompt Engineering", "Vector Databases", "Large Language Models (LLMs)", "NLP", "MLOps", "Salesforce Service Cloud Voice", "Amazon Q"]
    tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in ml_skills])
    st.markdown(tags, unsafe_allow_html=True)

    st.markdown("### Consulting & Leadership")
    leadership = ["Pre-Sales Engineering", "C-Level Executive Consultation", "Product-Market Fit (PMF)", "Agile Delivery", "RFI/RFP Management"]
    tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in leadership])
    st.markdown(tags, unsafe_allow_html=True)
