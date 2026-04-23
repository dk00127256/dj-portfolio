import streamlit as st

def render():
    st.title("Projects")
    
    # Project 1
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("### Goshti Ghar - Multilingual Audio Story Generator")
        st.markdown("""
        A robust, production-ready local-first storytelling platform that generates age-appropriate stories dynamically.
        Features an aggressive audio state cleanup and a FastAPI backend with strict input validation.
        """)
        st.markdown("[GitHub Repo](https://github.com/dj-kulkarni) | [Live Demo](#)")
        skills = ["FastAPI", "React", "Generative AI", "Python", "TypeScript"]
        tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
        st.markdown(tags, unsafe_allow_html=True)
    with col2:
        st.image("https://via.placeholder.com/300x200", caption="Goshti Ghar Thumbnail")
        
    st.markdown("---")
    
    # Project 2
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("### Amazon Connect - IT Helpdesk")
        st.markdown("""
        Integrated advanced Amazon Connect Contact Lens rules for real-time chat and post-chat analysis. Deployed comprehensive real-time metrics and agent evaluation forms via CloudFormation.
        """)
        st.markdown("[GitHub Repo](https://github.com/dj-kulkarni)")
        skills = ["Amazon Connect", "AWS CloudFormation", "Contact Lens", "CCaaS"]
        tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
        st.markdown(tags, unsafe_allow_html=True)
    with col2:
        st.image("https://via.placeholder.com/300x200", caption="Amazon Connect Flow")

    st.markdown("---")
    
    # Project 3
    col1, col2 = st.columns([3, 2])
    with col1:
        st.markdown("### Connect Flow Deployer")
        st.markdown("""
        An automated deployment pipeline for managing and deploying complex Amazon Connect flows seamlessly across different environments.
        """)
        st.markdown("[GitHub Repo](https://github.com/dj-kulkarni)")
        skills = ["AWS", "CI/CD", "Automation", "Amazon Connect"]
        tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
        st.markdown(tags, unsafe_allow_html=True)
    with col2:
        st.image("https://via.placeholder.com/300x200", caption="Connect Flow Deployer")
