import requests
from bs4 import BeautifulSoup

def scrape_skills(job_link):


    if "prospects" in str(job_link):
        ##If it is a prospects.ac link

        new_page = requests.get(job_link)
        new_soup = BeautifulSoup(new_page.content, 'html.parser')

        skills_title = new_soup.find("h2",{ "id" : "skills"})
        random_text = skills_title.find_next_sibling()
        skills = random_text.find_next_sibling()

        skills_text=[]

        for skill in skills:
            skills_text.append(skill)

        return skills_text


    else:
        job_description = ""

        page = requests.get(job_link)
        soup = BeautifulSoup(page.content, 'html.parser')

        content = soup.findAll("p")
        # print(content[1:3])
        for i in content[1:3]:
            job_description += i.getText()
            job_description += " "

        skills_text=[]

        return skills_text