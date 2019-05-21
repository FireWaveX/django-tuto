import schedule
import time
import urllib.request
from subprocess import check_output


# r = urllib.request.urlopen("http://localhost:8000/users/?format=json").read()


def job():
    # print(r)
    check_output("py manage.py test pools", shell=True)

schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)