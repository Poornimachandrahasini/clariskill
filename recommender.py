import pandas as pd

def load_skills_data(filepath):
    """Loads skills dataset from a CSV and returns a dict."""
    df = pd.read_csv(filepath)
    skills_data = {}
    for _, row in df.iterrows():
        role = row['Role']
        skills = [skill.strip() for skill in row['Skills'].split(';') if skill.strip()]
        skills_data[role] = skills
    return skills_data

def analyze_skills(user_skills, target_role, role_skills_data):
    """Returns matched skills, missing skills, and match score."""
    required_skills = role_skills_data.get(target_role, [])
    matched = [skill for skill in user_skills if skill in required_skills]
    missing = [skill for skill in required_skills if skill not in user_skills]
    score = round((len(matched) / len(required_skills)) * 100) if required_skills else 0
    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "score": score
    }
