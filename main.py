from bs4 import BeautifulSoup
import requests
import time

def job_posts():
    html_text = requests.get('https://www.brightermonday.co.ke/jobs').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('article', class_ ='search-result')
    for index, job in enumerate(jobs):
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
        # save in directory
        with open(f'job posts/{index}','w') as f:
            f.write(f"Company name:{company_name.strip()}\n ")
            f.write(f"Job position:{position}\n")
            f.write(f"Job Function:{job_fn}\n")
        print(f'file saved: {index}')

if __name__ == '__main__':
    while True:
        job_posts()
        time_wait = 20
        print(f'waiting{time_wait}minutes...')
        time.sleep(time_wait * 60)

