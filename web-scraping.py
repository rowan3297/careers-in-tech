from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/Web')
def index():
    url = 'https://www.totaljobs.com/advice/software-developer-job-description'
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    content = soup.find('div', class_='content').get_text()  
    return render_template('index.html', content=content)

# url = "https://www.totaljobs.com/advice/software-developer-job-description"

# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.content, "html.parser")
#     page_content = soup.find("section",class_="piece-content")
#     print(page_content)


# else:
#     print("Failed to retrieve job listings. Status code:", response.status_code)