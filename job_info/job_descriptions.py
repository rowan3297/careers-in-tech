import requests
from bs4 import BeautifulSoup

def scrape_description(job_link):


    if "prospects" in str(job_link):
        ##If it is a prospects.ac link

        new_page = requests.get(job_link)
        new_soup = BeautifulSoup(new_page.content, 'html.parser')
                
        ##Finds the job description from within the given pages parsed html

        for page_content in new_soup.findAll('div',class_='content'):
            job_descriptionRaw = list(page_content.children)[1]
            job_description = job_descriptionRaw.getText()

        return job_description


    else:
        job_description = ""

        page = requests.get(job_link)
        soup = BeautifulSoup(page.content, 'html.parser')

        content = soup.findAll("p")
        # print(content[1:3])
        for i in content[1:3]:
            job_description += i.getText()
            job_description += " "

        return job_description



## Use something like getRoleId in the python helpers file to figure out what job has been clicked on?