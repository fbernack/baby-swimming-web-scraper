import requests
from bs4 import BeautifulSoup
import re

base = "https://shop.fresch-freising.de"
courses_url = base + "/courses/5"
file_path = "courses.md"

# get website contents and parse html
response = requests.get(courses_url)
html = BeautifulSoup(response.text, 'html.parser')

categories_html = html.find('section', {"id" : "Categories"})
courses_html = categories_html.findChildren("div", id=re.compile('^Course-'))

# create markdown string of courses
courses_markdown = "# Babyschwimmen Kursübersicht"
for t in courses_html:
    # parse information
    headline = t.find('h5', {"class" : "card-title"}).text
    text = t.find('p').text
    url = base + t.find('a' ,href=True)['href']
    
    # Strip whitespaces
    headline_stripped = re.sub(' +', ' ', headline).strip()
    text_stripped = re.sub(' +', ' ', text).strip()
    
    # append to markdown
    courses_markdown += """
## {}
[{}]({})
""".format(headline_stripped, text_stripped, url)

# open yaml file for reading
with open(file_path, "r") as courses_file:
    saved_courses = courses_file.read()
    # check if there is an update
    if saved_courses == courses_markdown:
        print("no new courses")
    else:
        print("new courses")
        
# open file for writing
with open(file_path, "w") as courses_file:
    courses_file.write(courses_markdown)
