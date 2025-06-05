import streamlit as st
import matplotlib.pyplot as plt
from recommender import load_skills_data, analyze_skills

# Streamlit page config
st.set_page_config(page_title="ClarSkill - Turning Confusion Into Clarity", layout="centered")

# ✅ Gradient Background & Styled Text
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #e0c3fc, #8ec5fc);
        color: #2e2e2e;
    }
    header, footer, [data-testid="stToolbar"] {
        visibility: hidden;
    }
    .stTextInput > div > div > input,
    .stSelectbox > div > div > div > div {
        background-color: #ffffffcc;
        color: #000;
    }
    .stButton > button {
        background-color: #6a11cb;
        color: white;
    }
    h1, h2, h3, h4, h5 {
        color: #2c003e;
    }
    .stMetric {
        color: #111;
    }
    </style>
""", unsafe_allow_html=True)

# App Title and Intro
st.title("🎯 ClarSkill - Turning Confusion Into Clarity")
st.write("Analyze your current skills and get personalized career-ready recommendations!")

# Load skill data
role_skills = load_skills_data('skills_dataset.csv')

# User Inputs
name = st.text_input("👩‍🎓 Your Name")
branch = st.selectbox("📚 Your Branch", ["CSE", "ECE", "EEE", "MECH", "CIVIL", "Other"])
year = st.selectbox("📆 Your Year", ["1st", "2nd", "3rd", "4th"])

st.subheader("🧠 Select Your Current Skills")
all_skills = ['Python', 'C', 'C++', 'Java', 'SQL', 'HTML', 'CSS', 'JavaScript',
              'Machine Learning', 'Data Analysis', 'Cloud Computing', 'Git', 'DSA']
selected_skills = st.multiselect("Choose all that apply", all_skills)

st.subheader("🚀 Select Your Target Career")
career_roles = ['Data Scientist', 'Web Developer', 'Software Engineer', 'Cloud Engineer', 'AI Engineer']
selected_role = st.selectbox("Choose your goal", career_roles)

# Analyze Button
if st.button("🔍 Analyze My Skills"):
    if not name:
        st.error("Please enter your name.")
    elif not selected_skills:
        st.error("Please select at least one skill.")
    else:
        result = analyze_skills(selected_skills, selected_role, role_skills)
        st.success(f"Thank you {name}! Here's your skill analysis for the role: {selected_role}")

        # Skill Score
        st.subheader("📊 Skill Score")
        st.metric(label="Skill Match Score (%)", value=result['score'])

        # Chart selection
        st.subheader("📈 Skill Match Overview - Choose Your Chart Type")
        chart_type = st.selectbox("Select Chart Type", ["Pie Chart", "Bar Chart", "Horizontal Bar", "Line Chart", "Donut Chart"])

        matched = len(result['matched_skills'])
        missing = len(result['missing_skills'])

        labels = ['Matched Skills', 'Missing Skills']
        sizes = [matched, missing]
        colors = ['#4CAF50', '#F44336']

        fig, ax = plt.subplots()

        if chart_type == "Pie Chart":
            ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            ax.axis('equal')
        elif chart_type == "Bar Chart":
            ax.bar(labels, sizes, color=colors)
            ax.set_ylabel("Number of Skills")
            ax.set_title("Bar Chart of Skill Match")
        elif chart_type == "Horizontal Bar":
            ax.barh(labels, sizes, color=colors)
            ax.set_xlabel("Number of Skills")
            ax.set_title("Horizontal Bar Chart of Skill Match")
        elif chart_type == "Line Chart":
            ax.plot(labels, sizes, marker='o', linestyle='-', color='purple')
            ax.set_ylabel("Number of Skills")
            ax.set_title("Line Chart of Skill Match")
        elif chart_type == "Donut Chart":
            wedges, texts, autotexts = ax.pie(
                sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90,
                wedgeprops=dict(width=0.5)
            )
            ax.set_title("Donut Chart of Skill Match")
            ax.axis('equal')

        # Show the chart
        st.pyplot(fig)

        # Matched & Missing Skills
        st.subheader("✅ Skills You Have")
        st.write(", ".join(result['matched_skills']) if result['matched_skills'] else "None")

        st.subheader("⚠️ Skills You Should Learn")
        st.write(", ".join(result['missing_skills']) if result['missing_skills'] else "You have all required skills!")

        # Learning Resources
        st.subheader("📚 Learning Resources for Missing Skills")
        resource_links = {
            "CSS": "https://developer.mozilla.org/en-US/docs/Web/CSS",
            "Git": "https://learngitbranching.js.org/",
            "JavaScript": "https://www.javascript.com/learn",
            "Node.js": "https://nodejs.dev/learn",
            "React": "https://react.dev/learn",
            "Python": "https://www.learnpython.org/",
            "Machine Learning": "https://www.coursera.org/learn/machine-learning",
            "Data Analysis": "https://www.datacamp.com/courses/introduction-to-data-analysis-in-python",
            "SQL": "https://www.w3schools.com/sql/",
            "HTML": "https://developer.mozilla.org/en-US/docs/Web/HTML",
            "C": "https://www.learn-c.org/",
            "C++": "https://cplusplus.com/doc/tutorial/",
            "Java": "https://www.codecademy.com/learn/learn-java",
            "DSA": "https://www.geeksforgeeks.org/data-structures/",
            "Cloud Computing": "https://www.ibm.com/training/cloud",
            "Docker": "https://docker-curriculum.com/",
            "Kubernetes": "https://kubernetes.io/docs/tutorials/",
            "AWS": "https://aws.amazon.com/training/",
            "Linux": "https://linuxjourney.com/",
            "Scikit-learn": "https://scikit-learn.org/stable/tutorial/index.html",
            "TensorFlow": "https://www.tensorflow.org/learn",
            "PyTorch": "https://pytorch.org/tutorials/",
            "Mathematics": "https://www.khanacademy.org/math/statistics-probability"
        }

        for skill in result['missing_skills']:
            if skill in resource_links:
                st.markdown(f"- [{skill}]({resource_links[skill]})")

# ✅ Footer
st.markdown("""
<hr style="margin-top: 50px;">
<div style='text-align: center; color: gray; font-size: 14px;'>
    ❤️ Created by ClarSkill
</div>
""", unsafe_allow_html=True)
