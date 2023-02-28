import schedule
import time


def func():
    print("Geeksforgeeks")


schedule.every(5).minutes.do(func)

while True:
    schedule.run_pending()
    time.sleep(1)