import streamlit as st
from streamlit_option_menu import option_menu

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

import views.about_me as about_me
import views.experience as experience
import views.technical_skills as technical_skills
import views.education as education
import views.certifications as certifications
import views.projects as projects
import views.blogs as blogs
import views.volunteering as volunteering
import views.contact as contact
import views.awards as awards
import views.photo_gallery as photo_gallery

# Page config
st.set_page_config(
    page_title="My Portfolio",
    page_icon="👋",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.image("Profile Pic.HEIC", width=150)
    st.markdown("### Dhananjay (DJ) Kulkarni")
    st.markdown("CCaaS Specialist, GenAI, AI/ML, Cloud Architect, Technical Project Management")
    
    selected = option_menu(
        menu_title=None,
        options=["About Me", "Experience", "Technical Skills", "Education", "Certifications", "Projects", "Blogs", "Volunteering", "Awards", "Photo Gallery", "Contact"],
        icons=["person", "briefcase", "code-slash", "book", "patch-check", "folder", "journal-text", "heart", "trophy", "camera", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "transparent"},
            "icon": {"color": "#0EA5E9", "font-size": "18px"}, 
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#334155", "color": "#CBD5E1"},
            "nav-link-selected": {"background-color": "rgba(14, 165, 233, 0.15)", "color": "#0EA5E9", "border-right": "3px solid #0EA5E9"},
        }
    )
    
    st.markdown("---")
    st.markdown("### Connect")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/dj-kulkarni) | [GitHub](https://github.com)")

# Main Content Router
if selected == "About Me":
    about_me.render()
elif selected == "Experience":
    experience.render()
elif selected == "Technical Skills":
    technical_skills.render()
elif selected == "Education":
    education.render()
elif selected == "Certifications":
    certifications.render()
elif selected == "Projects":
    projects.render()
elif selected == "Blogs":
    blogs.render()
elif selected == "Volunteering":
    volunteering.render()
elif selected == "Awards":
    awards.render()
elif selected == "Photo Gallery":
    photo_gallery.render()
elif selected == "Contact":
    contact.render()
