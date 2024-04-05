# Scraping the given url

Scraped the given url and get the given rows and column through BeautifulSoup and also added the background task schedular celery which will run every midnight 
and save the data in the database.

# Local Setup-

git clone url
create a .env file in root directory
to start run command: sudo systemctl restart nginx
to check status run command: sudo systemctl status  nginx

# Tech Stack

python
Django
Sqllite
Celery
Nginx
