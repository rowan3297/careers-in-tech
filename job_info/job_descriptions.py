import requests
from bs4 import BeautifulSoup

def scrape_description(job):

    url = "https://www.prospects.ac.uk/job-profiles/browse-a-to-z"
    base_url = "https://www.prospects.ac.uk"
    # url = 'https://www.totaljobs.com/advice/software-developer-job-description'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")


    ## Returns the link for a given job where the job title must be in the form "Aaaa... aaaaaa..."
    for a in soup.findAll('a',href=True):
        if job in a.text:
            new_url = base_url+ a["href"]

    new_page = requests.get(new_url)
    new_soup = BeautifulSoup(new_page,'html.parser')
            
    ##Finds the job description from within the given pages parsed html

    for page_content in new_soup.findAll('div',class_='content'):
        job_descriptionRaw = list(page_content.children)[1]
        job_description = job_descriptionRaw.getText()

    return job_description

## Use something like getRoleId in the python helpers file to figure out what job has been clicked on?