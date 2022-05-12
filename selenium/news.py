import schedule
import time
import os


def job():
    print(datetime.datetime.now())
    print("I'm working...")


schedule.every().day.at("13:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
