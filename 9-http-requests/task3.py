import requests
from datetime import date, timedelta, datetime

HOST = 'https://api.stackexchange.com/2.3'

day_before_yesterday = (datetime.today() - timedelta(days=2)).timestamp().__round__()

resp = requests.get(HOST + '/questions',
                    params={'fromdate': day_before_yesterday, 'tagged': 'Python', 'site': 'stackoverflow'})

resp.raise_for_status()
questions = resp.json()["items"]

print(f"Number of questions: {len(questions)}")
for question in questions:
    print(question["title"])
