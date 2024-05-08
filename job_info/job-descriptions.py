import requests
from bs4 import BeautifulSoup

url = "https://www.prospects.ac.uk/job-profiles/browse-a-to-z"
base_url = "https://www.prospects.ac.uk"
# url = 'https://www.totaljobs.com/advice/software-developer-job-description'

## Returns the parsed html for a given url
def getLinkSoup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


## Returns the link for a given job where the job title must be in the form "Aaaa... aaaaaa..."
def find_jobLink(soup):
    for a in soup.findAll('a',href=True):
        if job_title in a.text:
            new_url = base_url+ a["href"]
            return new_url
        
##Finds the job description from within the given pages parsed html
def find_jobDesc(soup):
    for page_content in soup.findAll('div',class_='content'):
        job_descriptionRaw = list(page_content.children)[1]
        job_description = job_descriptionRaw.getText()
        return job_description
## Example code for a business analyst role
job_title = "Business analyst"
soup = getLinkSoup(url)
            
new_link = find_jobLink(soup)

new_page = requests.get(new_link)
new_soup = BeautifulSoup(new_page.content,"html.parser")

job_description = find_jobDesc(new_soup)
print(job_description)

## Use something like getRoleId in the python helpers file to figure out what job has been clicked on?