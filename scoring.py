from utils_openai import cosine_similarity, llm_response

def enlist(json_data):
    # Extracting Skills
    skills = [skill['name'] for skill in json_data.get('skills', [])]

    # Extracting Education
    education_data = json_data.get('education', [])
    if isinstance(education_data, list):
        education = [{
            # "school": edu['school'],
            "degree": edu['degree'],
            "fieldOfStudy": edu.get('fieldOfStudy', ''),
            # "startDate": edu.get('startDate', ''),
            # "endDate": edu.get('endDate', '')
        } for edu in education_data]
    else:
        education = [{
            #"school": education_data.get('school', ''),
            "degree": education_data.get('degree', ''),
            "fieldOfStudy": education_data.get('fieldOfStudy', ''),
            # "startDate": education_data.get('startDate', ''),
            # "endDate": education_data.get('endDate', '')
        }]

    work_experience_data = json_data.get('workExperience', [])

    if isinstance(work_experience_data, list):
        work_experience = [{
            #"company": exp['company'],
            "position": exp['position'],
            "description" : exp['description']
        } for exp in work_experience_data]
        work_desc = [exp['description'] for exp in work_experience_data]
    else:
        work_experience = [{
            #"company": work_experience_data.get('company', ''),
            "position": work_experience_data.get('position', '')
        }]
        work_desc = [work_experience_data.get('description', '')]

    # Extracting Descriptions of Projects
    project = [project['name'] for project in json_data.get('projects', [])]
    project_desc = [project['description'] for project in json_data.get('projects', [])]


    # Extracting Certifications
    certifications = [cert['name'] for cert in json_data.get('certifications', [])]
    cert_desc = [cert['description'] for cert in json_data.get('certifications', [])]


    # Printing the extracted sections
    print("Skills:", skills)
    print("\nEducation:", education)
    print("\nWork Experience:", work_experience)
    print("\nWork Experience:", work_desc)
    print("\nProjects:", project)
    print("\nProject Descriptions:", project_desc)
    print("\nCertifications:", certifications)
    print("\nCertificate Description:", cert_desc)

    return skills, education, work_experience, work_desc, project, project_desc, certifications, cert_desc


def desc_scorer(desc,jd):
  jd_max = llm_response(f'''I have this Job Description:{jd}
                        The following text is an excerpt from the resume of a candidate for this job: {desc} Does this text display any characteristic or skill required by the JD?
                        Please give output as either 0 or 1 only and nothing else.
                        ''')
  return int(jd_max)


def calculate_resume_score(skills, education, work_experience, work_desc, project, project_desc, certifications, cert_desc, jd):
    # Define the list of aspects to loop through
    aspects = [skills, education, work_experience, project, certifications]
    aspect_names = ["Skills", "Education", "Work Experience", "Projects", "Certifications"]
    description_aspects = [work_desc, project_desc, cert_desc]
    description_names = ["Work Experience Descriptions", "Project Descriptions", "Certificate Descriptions"]
    queries = jd
    used_queries = set()
    matches = {i: 0 for i in range(len(aspects))}
    max_scores = {i: 0 for i in range(len(aspects))}
    description_matches = {i: 0 for i in range(len(description_aspects))}
    description_max_scores = {i: 0 for i in range(len(description_aspects))}
    description_scores = {}
    aspect_scores = {}

    # Process non-description aspects
    for i, aspect_data in enumerate(aspects):
        query_list = queries.get(aspect_names[i], [])
        max_scores[i] = len(query_list)
        for query in query_list:
            if query in used_queries:
                continue

            if not aspect_data:
                continue

            # Skills list
            if isinstance(aspect_data, list) and all(isinstance(elem, str) for elem in aspect_data):
                for item in aspect_data:
                    similarity = cosine_similarity(item, query)

                    if similarity > 0.8:
                        matches[i] += 1
                        used_queries.add(query)
                        break

            combined_strings = ['\n'.join(f"{key}: {value}" for key, value in item.items()) for item in aspect_data if isinstance(item, dict)]

            for string in combined_strings:
                text1 = str(string)
                text2 = query
                similarity = cosine_similarity(text1, text2)

                if similarity > 0.8:
                    matches[i] += 1
                    used_queries.add(query)
                    break

    # Process description aspects with desc_score()
    for i, aspect_data in enumerate(description_aspects):
        query_list = queries.get(description_names[i], [])
        description_max_scores[i] = len(query_list)
        for query in query_list:
            description_matches[i] += desc_scorer(aspect_data, query)  # desc_score needs to be defined elsewhere

    overall_score = 0
    max_possible_score = 0
    aspect_weights = {'Skills': 1, 'Education': 1, 'Work Experience': 1, 'Projects': 2, 'Certifications': 2}

    # Calculate scores for non-description aspects
    for i, match_count in matches.items():
        aspect_name = aspect_names[i]
        score = match_count * aspect_weights.get(aspect_name, 1)
        max_score = max_scores[i] * aspect_weights.get(aspect_name, 1)
        overall_score += score
        max_possible_score += max_score
        print(f"Matches in {aspect_name}: {match_count}")
        print(f"Score for {aspect_name}: {score}")
        aspect_scores[aspect_name] = {"Match Count": match_count, "Score": score, "Max Score": max_score}

    # Calculate scores for description aspects
    description_aspects = [work_desc, project_desc, cert_desc]
    description_jd_texts = [jd['Work Experience Descriptions'], jd['Project Descriptions Text'], jd['Certificate Descriptions']]
    description_names = ["Work Experience Descriptions", "Project Descriptions", "Certificate Descriptions"]

    for desc, jd_text, desc_name in zip(description_aspects, description_jd_texts, description_names):
        desc_score_result = desc_scorer('\n'.join(desc), jd_text)
        description_scores[desc_name] = desc_score_result
        print(f'Score of {desc_name}: {desc_score_result}')
        overall_score += desc_score_result
        #max_possible_score += 10  # assuming each description aspect has a max score of 10

    #final_score_percentage = (overall_score / max_possible_score) * 100 if max_possible_score > 0 else 0
    print(f"Overall Score: {overall_score}")
    #print(f"Maximum Possible Score: {max_possible_score}")
    #print(f"Final Score as a Percentage: {final_score_percentage:.2f}%")

    # Return the final score
    return overall_score, aspect_scores, description_scores