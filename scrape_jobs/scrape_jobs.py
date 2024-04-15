import requests
from bs4 import BeautifulSoup as bs
import json
import time

def scrape_page(i):
    url = "https://leeds.tech/jobs/page/{}/?vacancy_type&cat=0&keywords#038;cat=0&keywords"
    content = None
    content = requests.get(url.format(i)).text
    # wait here for the result to be available before continuing
    while content is None:
        time.sleep(3)

    if len(content) > 0:
        soup = bs(content, features="html.parser")
        l = []
        for job in soup.find_all('div', {'class': 'posts-loop__item'}):
            title = [ h2.find('a').text for h2 in job.find_all('h2', {'class': 'posts-loop__item__title'}) ][0]
            url = [ h2.find('a').get('href') for h2 in job.find_all('h2', {'class': 'posts-loop__item__title'}) ][0]
            text = [ div.find('p').text for div in job.find_all('div', {'class': 'jobs-loop__item__text-container'}) ][0]
            l.extend([{"title": title, "url": url, "text": text}])

        with open("../data/leeds-tech-pt{}.json".format(i), "w") as out:
            json.dump(l, out, indent=4)

all_data = []
for i in range(1,17):
    with open("../data/20201026/leeds-tech-pt{}.json".format(i), "r") as infile:
        data = json.load(infile)
        all_data.extend(data)
with open("../data/20201026/tech-roles.json", "w") as out:
    json.dump(all_data, out, indent=4)
#
#print(len(data))
#print(data[0])

