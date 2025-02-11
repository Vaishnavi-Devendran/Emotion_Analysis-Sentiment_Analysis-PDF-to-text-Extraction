from templates import jd, required_skills
from mongo_utils import find_matching_resumes
from scoring import calculate_resume_score, enlist
import pandas as pd


shortlisted = find_matching_resumes(required_skills)

columns = ["Name", "Phone", "Websites", "emails", "City", "State", "DOB", "skills", "education", "work_ex", "work_desc", "projects", "project_desc", "certifications", "Total"]

df = pd.DataFrame(columns=columns)

for resume in shortlisted:
    skills, education, work_experience, work_desc, project, project_desc, certifications, cert_desc = enlist(resume)
    overall_score, aspect_scores, description_scores = calculate_resume_score(skills, education, work_experience, work_desc, project, project_desc, certifications, cert_desc, jd)

    new_row = {
        "Name": resume['name'],
        "Phone": resume['phoneNumbers'],
        "Websites": resume['websites'],
        "emails": resume['emails'],
        "City": resume['addresses']['city'],
        "State": resume['addresses']['state'],
        "DOB": resume['dateOfBirth'],
        "skills": aspect_scores['Skills']['Match Count'],
        "education": aspect_scores['Education']['Match Count'],
        "work_experience": aspect_scores['Work Experience']['Match Count'],
        "work_desc": description_scores['Work Experience Descriptions'],
        "projects": aspect_scores['Projects']['Match Count'],
        "project_desc": description_scores['Project Descriptions'],
        "certifications": aspect_scores['Certifications']['Match Count'],
        "cert_desc": description_scores['Certificate Descriptions'],
        "Total": overall_score
    }

    df = df.append(new_row, ignore_index=True)