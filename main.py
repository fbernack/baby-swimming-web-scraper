import requests
from bs4 import BeautifulSoup
import re

base = "https://shop.fresch-freising.de"
courses_url = base + "/courses/5"

# get website contents and parse html
response = requests.get(courses_url)
html = BeautifulSoup(response.text, 'html.parser')

categories_html = html.find('section', {"id" : "Categories"})
courses_html = categories_html.findChildren("div", id=re.compile('^Course-'))

# create markdown string of courses
courses_markdown = "# Babyschwimmen Kursübersicht"
for c in courses_html:
    # parse information
    headline = c.find('h5', {"class" : "card-title"}).text
    text = c.find('p').text
    url = base + c.find('a' ,href=True)['href']
    
    # Strip whitespaces
    headline_stripped = re.sub(' +', ' ', headline).strip()
    text_stripped = re.sub(' +', ' ', text).strip()
    
    # append to markdown
    courses_markdown += """
## {}
[{}]({})
""".format(headline_stripped, text_stripped, url)
      
# write markdown file
with open("courses.md", "w") as courses_file:
    courses_file.write(courses_markdown)
