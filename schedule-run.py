from healthcheck import sender
import schedule
from datetime import date
import time 
import sys
def job():
    f = open('credentials.csv', 'r')
    credentials = f.read().split('\n')
    for i in credentials:
        try:
            udata = i.split(',')
            catcher = sender(udata[0], udata[1], udata[2])
            today = date.today()
            print(catcher + " " + str(today))
        except:
            print('exception occured')
if sys.argv[1] == 'schedule':
    schedule.every().day.at("07:30").do(job)
    while True:
        schedule.run_pending()
        time.sleep(30)
elif sys.argv[1] == 'run':
    job()
else:
    pass
    