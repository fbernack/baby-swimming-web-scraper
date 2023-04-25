import requests
from bs4 import BeautifulSoup
import re
import yaml

base = "https://shop.fresch-freising.de"
courses_url = base + "/courses/5"
file_path = "courses.yml"

# get website contents and parse html
response = requests.get(courses_url)
html = BeautifulSoup(response.text, 'html.parser')

categories_html = html.find('section', {"id" : "Categories"})
courses_html = categories_html.findChildren("div", id=re.compile('^Course-'))

# create list of courses
courses = []
for t in courses_html:
    headline = t.find('h5', {"class" : "card-title"}).text
    text = t.find('p').text
    
    # Strip whitespaces within text
    headline_stripped = re.sub(' +', ' ', headline).strip()
    text_stripped = re.sub(' +', ' ', text).strip()
    url = base + t.find('a' ,href=True)['href']
    course = {
        "course": headline_stripped,
        "description": text_stripped,
        "link": url
    }
    courses.append(course)

# open yaml file for reading
with open(file_path, "r") as courses_file:
    saved_courses = yaml.safe_load(courses_file)
    # check if there is an update
    if saved_courses == courses:
        print("no new courses")
    else:
        print("new courses")
        
# open file for writing
with open(file_path, "w") as courses_file:
    courses_file.write(yaml.dump(courses))
