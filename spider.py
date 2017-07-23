import os
import requests
import time
from models import db, Job
from settings import QUERY, TOKEN, CHAT_ID, BASE_URL, DB_FILE, RESOURCES_DIR
import telegram
import logging

url = f'{BASE_URL}?limit=5&offset=0&query={QUERY}'
DELAY = 60
logging.basicConfig(filename=os.path.join(RESOURCES_DIR, 'spider.log'))


def init_db():
    if not os.path.exists(DB_FILE):
        db.connect()
        db.create_table(Job)


def _save_job(job):
    created = time.ctime(job['created'] / 1000)
    return Job.create(
        title=job['title'],
        created=created,
        job_id=job['id'],
        description=job['description'],
        budget=job['budget'])


def process(resp, bot):
    for job in resp['jobs']:
        job_query = Job.select().where(Job.job_id == job['id'])
        if job_query.exists():
            continue
        else:
            job = _save_job(job)
            try:
                bot.send_message(
                    chat_id=CHAT_ID, text=job.to_text(), parse_mode='Markdown')
            except Exception:
                logging.exception()


if __name__ == '__main__':
    init_db()
    while True:
        bot = telegram.Bot(TOKEN)
        resp = requests.get(url).json()
        if resp:
            process(resp, bot)
        time.sleep(DELAY)
