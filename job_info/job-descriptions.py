import requests
from bs4 import BeautifulSoup

url = "https://www.prospects.ac.uk/job-profiles/browse-a-to-z"
base_url = "https://www.prospects.ac.uk"
# url = 'https://www.totaljobs.com/advice/software-developer-job-description'

page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

job_title = "Business analyst"

def getLinkSoup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup


def find_jobLink(soup):
    for a in soup.findAll('a',href=True):
        if job_title in a.text:
            new_url = base_url+ a["href"]
            return new_url
            
new_link = find_jobLink(soup)

new_page = requests.get(new_link)
new_soup = BeautifulSoup(new_page.content,"html.parser")
print(new_soup.prettify)