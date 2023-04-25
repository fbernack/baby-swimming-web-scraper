# baby-swimming-web-scraper

Web scraper including GitHub action to retrieve new appointments for baby swimming courses from a website every hour and send them via email if needed. Can be used as a template for your own web scraper as well as scheduled tasks.

## Usage

1. *(Optional)* Setup & activate virtual environment

        python3 -m venv ./env
        source ./env/bin/activate

2. Install required modules

        pip install requests
        pip install beautifulsoup4
        pip install pyyaml

3. Execute web scraper
   
        python main.py

## Note
`pipereqs` is used for creating the `requirements.txt`. 

    pip install pipreqs
    pipreqs /path/to/project