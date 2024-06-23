import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/jobs/search/?keywords=admin&location=Jakarta%2C%20Indonesia'
response = requests.get(url)

Soup = BeautifulSoup(response.text, 'html.parser')

job_listings = Soup.find_all('div', {'class': 'base-card'})

with open('hasil.txt', 'w') as file:
    for listing in job_listings:
        title = listing.find('h3').text.strip()
        company = listing.find('h4').text.strip()
        location = listing.find('span', {'class': 'job-search-card__location'}).text.strip()
        date_posted = listing.find('time').text.strip()

        file.write(f'Title: {title}\n')
        file.write(f'Company: {company}\n')
        file.write(f'Location: {location}\n')
        file.write(f'Date Posted: {date_posted}\n')
        file.write('\n')

print('Wah udah selesai nih , datanya di save di hasil.txt')
