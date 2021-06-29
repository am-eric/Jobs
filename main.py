from bs4 import BeautifulSoup
import requests


html_text = requests.get('https://www.brightermonday.co.ke/jobs').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('article', class_ ='search-result')
for job in jobs:
    try:
        position = job.find('h3').text
    except:
        pass

    try:
        company_name = job.find('div', class_='if-content-panel padding-lr-20 flex-direction-top-to-bottom--under-lg align--start--under-lg search-result__job-meta').text
    except:
        pass

    try:
        job_fn = job.find('span', class_='padding-lr-10 gutter-flush-under-lg').text
    except:
        pass

    print(f"Company name:{company_name.strip()} ")
    print(f"Job position:{position}")
    print(f"Job Function:{job_fn}\n")


