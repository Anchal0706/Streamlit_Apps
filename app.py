import streamlit as st
from PIL import Image

# Set page layout to wide
st.set_page_config(layout="wide")

# Title and Header with Photo Section
st.markdown("<h1 style='font-style: italic; text-align: center; font-family: cursive;'>Anchal Mishra</h1>", unsafe_allow_html=True)
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("<h2 style='font-style: italic; text-align: center;'>Content Analyst</h2>", unsafe_allow_html=True)

    st.markdown(
        "<p style='font-size: smaller; text-align: center;'>"

        "<b><a href='https://linkedin.com/in/anchal-mishra-b73109171' target='_blank'>LinkedIn</a></b> | "

        "<b><a href='mailto:anchalmishra028@gmail.com'>Email</a></b>"
                "</p>",

        unsafe_allow_html=True
    )
with col2:
    st.image("https://via.placeholder.com/150", caption="Your Photo", width=150)

# Profile Section in the center
st.markdown("<h2 style='font-style: italic; text-align: center;'>Profile</h2>", unsafe_allow_html=True)
st.markdown(
    "<div style='border: 2px solid #4A90E2; padding: 15px; border-radius: 10px;'>"
    "<p style='font-size: 16px;'>"
    "Content Analyst with a strong background in English Literature and Mass Communication, specializing in leveraging AI and data analytics to summarize, validate, and refine content effectively. Skilled in providing detailed feedback and annotations to enhance content quality. A creative, self-motivated professional proficient in Excel, Google Suite, and AI tools. Open to full-time opportunities."
    "</p>"
    "</div>",
    unsafe_allow_html=True
)
# **Horizontal Layout for Skills and Professional Experience**
st.markdown("<h2 style='font-style: italic; >Profile</h2>", unsafe_allow_html=True)
skills = [
    "Generative AI, LLM, Prompt Engineering",
    "Communication: English reading and writing comprehension",
    "Detailed annotations, Constructive feedback",
    "Research and analytical skills",
    "Creative and lateral thinking",
    "Adobe Illustrator, SEO",
    "Proficiency in Excel and Google Suite",
    "Hindi Typing"
]
col1, col2 = st.columns(2)

with col1:
    st.markdown("<h2 style='font-style: italic;'>Skills</h2>", unsafe_allow_html=True)

    st.markdown(

        "<div style='border: 2px solid #4A90E2; padding: 15px; border-radius: 10px;'>"
        "<ul style='font-size: 16px; list-style-type: none;'>"
        + "".join([f"<li>- {skill}</li>" for skill in skills]) +
        "</ul>"
        "</div>",
        unsafe_allow_html=True

    )

# Professional Experience Section (side by side)
experience = [
    ("Freelancer, Outlier.AI (2024/10 – Present)", [
        "- Experienced in training large language models (LLMs) to align with specific content requirements.",
        "- Applied RLHF and SFT techniques to improve content relevance and user satisfaction.",
        "- Optimized user experiences by collaborating with cross-functional teams."
    ]),
    ("Content Marketer, Qorvatech (2023/08 – 2024/09)", [
        "- Analyzed content requirements and created engaging articles.",
        "- Used AI tools like GPT to validate and summarize datasets."
    ])
]
with col2:

    st.markdown("<h2 style='font-style: italic;'>Professional Experience</h2>", unsafe_allow_html=True)
    st.markdown(
        "<div style='border: 2px solid #4A90E2; padding: 15px; border-radius: 10px;'>"
        + "".join([
            f"<h3>{title}</h3><ul style='font-size: 16px;'>"
            + "".join([f"<li>{item}</li>" for item in items]) +
            "</ul>" for title, items in experience
        ]) +
        "</div>",
        unsafe_allow_html=True
    )

# **Remaining sections remain unchanged, just with the appropriate color adjustments**

#Education Section in the center
st.markdown("<h2 style='font-style: italic; text-align: center;'>Education</h2>", unsafe_allow_html=True)
education = [
    ("Foreign Language Programme", "Indian Institute of Technology Kanpur (2024/08 – Present)"),
    ("Masters in Arts (English Literature)", "Kanpur University"),
    ("Diploma in Mass Communication", "Jagran Institute of Management and Mass Communications"),
    ("B.A.", "Jagran College of Arts, Science and Commerce")
]
st.markdown(
    "<div style='border: 2px solid #4A90E2; padding: 15px; border-radius: 10px;'>"
    + "".join([f"<b>{degree}</b><br>{institution}<br>" for degree, institution in education]) +
    "</div>",
    unsafe_allow_html=True
)
# Achievements in the center and section in box
st.markdown("<h2 style='font-style: italic; text-align: center;'>Achievements</h2>", unsafe_allow_html=True)
achievements = [
    "Named as Page Designer for the college magazine.",
    "Winner of the essay writing competition in an inter-college event.",
    "Served as House Captain and Class Monitor in school.",
    "Co-author of the anthology 'My Favorite Person'.",
    "Secured 2nd rank in the inter-college debate competition.",
    "Head of the Cultural Club at my college."
]
st.markdown(
    "<div style='border: 2px solid #4A90E2; padding: 15px; border-radius: 10px;'>"
    "<ul style='font-size: 16px; list-style-type: none;'>"
    + "".join([f"<li>- {achievement}</li>" for achievement in achievements]) +
    "</ul>"
    "</div>",
    unsafe_allow_html=True
)
#Languages Section in the center and in box
st.markdown("<h2 style='font-style: italic; text-align: center;'>Language</h2>", unsafe_allow_html=True) 
st.markdown(
    "<div style='border: 2px solid #4A90E2; padding: 15px; border-radius: 10px;'>"
    "<p style='font-size: 16px;'>English | French | Hindi</p>"
    "</div>",
    unsafe_allow_html=True
)
# Footer Section with Contact Button
st.markdown("---")
st.write("Designed and developed by Anchal Mishra")
# Contact Me Button
contact_me_html = """
<div style='display: flex; justify-content: center;'>
    <a href='mailto:anchalmishra028@gmail.com' target='_blank' style='text-decoration: none;'>
        <button style='background-color: #4A90E2; color: white; padding: 10px 20px; border: none; border-radius: 50px; font-size: 16px; cursor: pointer;'>
            Contact Me
        </button>
    </a>
</div>
"""
st.markdown(contact_me_html, unsafe_allow_html=True)
