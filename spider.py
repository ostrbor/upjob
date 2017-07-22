import requests
import time
from models import Job
from settings import QUERY, TOKEN, CHAT_ID, BASE_URL
import telegram

url = '%s?limit=5&offset=0&query=%s' % (BASE_URL, QUERY)


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
            bot.send_message(
                chat_id=CHAT_ID, text=job.to_text(), parse_mode='Markdown')


if __name__ == '__main__':
    while True:
        bot = telegram.Bot(TOKEN)
        resp = requests.get(url).json()
        if resp:
            process(resp, bot)
        time.sleep(25)
