import streamlit as st

# Set page layout to wide
st.set_page_config(layout="wide")

# Title and Header with Blank Photo Section
st.markdown("""
    <style>
        body {
            margin: 0;
            padding: 0;
        }
        h1, h2, h3, p {
            font-family: Arial, sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# Blank photo placeholder
st.markdown("<div style='text-align: center; height: 150px; width: 150px; border: 2px solid #4A90E2; border-radius: 50%; margin: 0 auto;'></div>", unsafe_allow_html=True)

# Title Section
st.markdown("<h1 style='text-align: center; font-size: 36px;'>Anchal Mishra</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-size: 24px;'>Content Analyst</h2>", unsafe_allow_html=True)

# Links Section
st.markdown("""
    <p style='text-align: center; font-size: 18px;'>
        <a href='https://linkedin.com/in/anchal-mishra-b73109171' target='_blank'><b>LinkedIn</b></a> |
        <a href='mailto:anchalmishra028@gmail.com'><b>Email</b></a>
    </p>
""", unsafe_allow_html=True)

# Profile Section
st.markdown("<h2 style='text-align: center;'>Profile</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style='border: 2px solid #4A90E2; padding: 15px; border-radius: 10px;'>
        <p style='font-size: 16px;'>
            Content Analyst with a strong background in English Literature and Mass Communication, specializing in leveraging AI and data analytics to summarize, validate, and refine content effectively. Skilled in providing detailed feedback and annotations to enhance content quality. A creative, self-motivated professional proficient in Excel, Google Suite, and AI tools. Open to full-time opportunities.
        </p>
    </div>
""", unsafe_allow_html=True)

# Skills and Professional Experience Sections
st.markdown("<h2 style='text-align: center;'>Professional Experience</h2>", unsafe_allow_html=True)
st.markdown("""
    <div style='border: 2px solid #4A90E2; padding: 15px; border-radius: 10px;'>
        <h3>Freelancer, Outlier.AI (2024/10 – Present)</h3>
        <ul>
            <li>Experienced in training large language models (LLMs) to align with specific content requirements.</li>
            <li>Applied RLHF and SFT techniques to improve content relevance and user satisfaction.</li>
            <li>Optimized user experiences by collaborating with cross-functional teams.</li>
        </ul>
        <h3>Content Marketer, Qorvatech (2023/08 – 2024/09)</h3>
        <ul>
            <li>Analyzed content requirements and created engaging articles for diverse platforms.</li>
            <li>Enhanced content accuracy and logic through constructive feedback and detailed annotations.</li>
            <li>Used AI tools like GPT to validate and summarize datasets, fine-tuning model accuracy.</li>
        </ul>
        <h3>Content Writer, C-incognito (2022/11 – 2023/08)</h3>
        <ul>
            <li>Developed high-quality articles and blogs, adhering to SEO best practices.</li>
            <li>Validated content for accuracy and coherence, increasing audience retention by 20%.</li>
            <li>Applied creative thinking to implement innovative content strategies.</li>
        </ul>
        <h3>Content Writer, KnitInfotech (2022/04 – 2022/10)</h3>
        <ul>
            <li>Conducted scenario analysis to optimize content relevance and provide actionable insights.</li>
            <li>Collaborated with teams to refine content strategies and improve performance.</li>
        </ul>
        <h3>Content Writer, Ballot Box (2020/09 – 2022/03)</h3>
        <ul>
            <li>Published insightful articles in newspapers like Dainik Jagran and Sahara.</li>
            <li>Conducted thorough research to create accurate and well-supported content.</li>
        </ul>
        <h3>Intern Content Writer, Vouchers Portal (2020/07 – 2020/08)</h3>
        <ul>
            <li>Engaged in content creation and digital marketing tasks, developing unique ideas.</li>
        </ul>
        <h3>Digital Marketing Intern, Rank Keywords (2020/05 – 2020/06)</h3>
        <ul>
            <li>Applied SEO techniques and analyzed website traffic to improve site rankings.</li>
        </ul>
        <h3>Intern in Brand Department, Dainik Jagran (2019/06 – 2019/07)</h3>
        <ul>
            <li>Supported brand management and promotional activities, contributing to strategic planning.</li>
        </ul>
        <h3>Freelancer, Profit by Click</h3>
        <ul>
            <li>Validated and summarized datasets using AI tools like GPT, fine-tuning model accuracy.</li>
            <li>Worked on various freelance projects, showcasing adaptability and meeting client-specific needs.</li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Skills Section
st.markdown("<h2 style='text-align: center;'>Skills</h2>", unsafe_allow_html=True)
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
st.markdown(
    "<div style='border: 2px solid #4A90E2; padding: 15px; border-radius: 10px;'>"
    "<ul style='list-style-type: none;'>"
    + "".join([f"<li>- {skill}</li>" for skill in skills]) +
    "</ul>"
    "</div>",
    unsafe_allow_html=True
)

# Achievements Section
st.markdown("<h2 style='text-align: center;'>Achievements</h2>", unsafe_allow_html=True)
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
    "<ul style='list-style-type: none;'>"
    + "".join([f"<li>- {achievement}</li>" for achievement in achievements]) +
    "</ul>"
    "</div>",
    unsafe_allow_html=True
)

# Education Section
st.markdown("<h2 style='text-align: center;'>Education</h2>", unsafe_allow_html=True)
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
st.write("Designed and developed by Anchal Mishra")
