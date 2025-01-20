import streamlit as st
from PIL import Image

# Title and Header with Photo Section
st.markdown("<h1 style='color: darkblue; font-style: italic;'>Anchal Mishra</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://via.placeholder.com/150", caption="Your Photo", width=150)
with col2:
    st.markdown("<h2 style='color: darkblue; font-style: italic;'>Content Analyst</h2>", unsafe_allow_html=True)
    st.write("### [LinkedIn](https://linkedin.com/in/anchal-mishra-b73109171) | [Email](mailto:anchalmishra028@gmail.com) | +91 8429745889")

# Profile Section
st.markdown("<h2 style='color: peru; font-style: italic;'>Profile</h2>", unsafe_allow_html=True)
st.write(
    "Content Analyst with a strong background in English Literature and Mass Communication, specializing in leveraging AI and data analytics to summarize, validate, and refine content effectively. Skilled in providing detailed feedback and annotations to enhance content quality. A creative, self-motivated professional proficient in Excel, Google Suite, and AI tools. Open to full-time opportunities."
)

# Skills Section
st.markdown("<h2 style='color: peru; font-style: italic;'>Skills</h2>", unsafe_allow_html=True)
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
st.write("\n".join(f"- {skill}" for skill in skills))

# Professional Experience Section
st.markdown("<h2 style='color: peru; font-style: italic;'>Professional Experience</h2>", unsafe_allow_html=True)
st.write("**Freelancer, Outlier.AI (2024/10 – Present)**")
st.write(
    "- Experienced in training large language models (LLMs) to align with specific content requirements.\n"
    "- Applied RLHF and SFT techniques to improve content relevance and user satisfaction.\n"
    "- Optimized user experiences by collaborating with cross-functional teams."
)

st.write("**Content Marketer, Qorvatech (2023/08 – 2024/09)**")
st.write(
    "- Analyzed content requirements and created engaging articles.\n"
    "- Used AI tools like GPT to validate and summarize datasets."
)

# Add more experience as needed...

# Education Section
st.markdown("<h2 style='color: peru; font-style: italic;'>Education</h2>", unsafe_allow_html=True)
st.write("**Foreign Language Programme**\nIndian Institute of Technology Kanpur (2024/08 – Present)")
st.write("**Masters in Arts (English Literature)**\nKanpur University")
st.write("**Diploma in Mass Communication**\nJagran Institute of Management and Mass Communications")
st.write("**B.A.**\nJagran College of Arts, Science and Commerce")

# Achievements Section
st.markdown("<h2 style='color: peru; font-style: italic;'>Achievements</h2>", unsafe_allow_html=True)
achievements = [
    "Named as Page Designer for the college magazine.",
    "Winner of the essay writing competition in an inter-college event.",
    "Served as House Captain and Class Monitor in school.",
    "Co-author of the anthology 'My Favorite Person'.",
    "Secured 2nd rank in the inter-college debate competition.",
    "Head of the Cultural Club at my college."
]
st.write("\n".join(f"- {achievement}" for achievement in achievements))

# Languages Section
st.markdown("<h2 style='color: peru; font-style: italic;'>Languages</h2>", unsafe_allow_html=True)
st.write("English | French | Hindi")

# Footer Section
st.markdown("---")
st.write("Designed and developed by Anchal Mishra")
