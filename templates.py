
jd_path = r'templates\jd.txt'

# Open the file and read its contents
try:
    with open(jd_path, 'r') as file:
        jd_text = file.read()
        
except FileNotFoundError:
    print(f"The file at {jd_path} was not found.")
    jd_text = None


import json

resume_template_path =  r'templates\resume_template_path.json'  

# Open the file and read the JSON content
try:
    with open(resume_template_path, 'r') as file:
        data = json.load(file)
        resume_template = data
except FileNotFoundError:
    print(f"The file at {resume_template_path} was not found.")
except json.JSONDecodeError:
    print(f"Error reading the JSON file at {resume_template_path}.")


prompt = ''' Please format the given resume to this JSON template only if the information is explicitly specified.
 If some fields like certificates are missing, don't just pass an empty list.
 Keep the structure of the key value pair intact, just put an empty string for each key only once.-->
 f'{resume_template}'

'''


jd_json_path = r'templates/jd.json'

try:
    with open(jd_json_path, 'r') as file:
        data = json.load(file)
        jd = data
except FileNotFoundError:
    print(f"The file at {jd_json_path} was not found.")
except json.JSONDecodeError:
    print(f"Error reading the JSON file at {jd_json_path}.")


jd["Work Experience Descriptions"] = jd_text
jd["Project Descriptions"] = jd_text
jd["Certificate Descriptions"] = jd_text





required_skills = [['SQL','Statistical Analysis','Data Analysis'], ['PowerBI','Business Analysis']]