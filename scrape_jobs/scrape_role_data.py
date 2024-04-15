import json
from serpstack.serp_stack import get_snippet

def load_jobs_data():
    with open('data/jobs_and_skills.json', 'r') as infile:
        jobs_array = json.load(infile)
    return jobs_data

def save_roles_data(roles_data):
    with open('data/roles.json', 'w') as outfile:
        json.dump(roles_data, outfile, indent=4)
    return

jobs_data = load_jobs_data()

roles = []
for job in jobs_data[0:10]:
    snippet = get_snippet( job['title'] )
    role = {}
    role['snippet'] = snippet[0]
    role['Url'] = snippet[1]
    role['job_id'] = job['id']
    roles.append(role)

save_roles_data(roles)
