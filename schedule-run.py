from healthcheck import sender
import schedule
from datetime import date
import time
def job():
    f = open('credentials.csv', 'r')
    credentials = f.read().split('\n')
    for i in credentials:
        udata = i.split(',')
        catcher = sender(udata[0], udata[1], udata[2])
        today = date.today()
        print(catcher + " " + str(today))
schedule.every().day.at("7:30").do(job)
while True:
    schedule.run_pending()
    time.sleep(30)
    