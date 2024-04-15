import json
#from app import mongo

def get_soft_skills_data():
    # TODO: don't handle data like this
    with open("app/data/wordlists.json", "r") as infile:
        data = json.load(infile)
        print("data")
    return data["soft_skills"]

def get_roles_data():
    # TODO: don't handle data like this
    with open("app/data/roles.json", "r") as infile:
        data = json.load(infile)
    return data

def get_jobs_data():
    # TODO: don't handle data like this
    with open("app/data/jobs_and_skills.json", "r") as infile:
        data = json.load(infile)
    return data

def get_users_array():
    # TODO: this is just for testing
    with open('app/data/users.json', 'r') as infile:
        users_array = json.load(infile)
    return users_array

def get_role_id(job_title):
    jobs_data = get_jobs_data()
    for job in jobs_data:
        if job['title'] == job_title:
            return job['id']
    return False

def get_role(title):
    role_id = get_role_id(title)
    roles_data = get_roles_data()
    for role in roles_data:
        if role['job_id'] == role_id:
            return role
    return False

def get_user(user_id):
    # get user details (TODO: not like this)
    user = mongo.db.users.find_one({"username": user_id})
    return user

def format_anon_user(form_data):
    """ create an anonymous user profile
        from the soft skills form data
    """
    anon_user = {
        "username": "anonymous",
        "soft_skills": {
                "creativity": int(form_data['creativity']),
                "organisation": int(form_data['organisation']),
                "collaboration": int(form_data['collaboration']),
                "numeracy": int(form_data['numeracy']),
                "communication": int(form_data['communication']),
                "literacy": int(form_data['literacy']),
                "versatile": int(form_data['versatile']),
                "emotional_intelligence": int(form_data['emotional_intelligence']),
                "leadership": int(form_data['leadership']),
                "analytical": int(form_data['analytical']),
                "keen_to_learn": int(form_data['keen_to_learn'])
        },
        "hard_skills": {"python":5}
    }
    return anon_user

def format_skills(skills_list):
    for i, skill in enumerate(skills_list):
        skills_list[i] = skill.split("|")[0].replace("_", " ")
    return skills_list
