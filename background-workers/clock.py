from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='sun', hour=20)
def update_job():
    print('this is a job')

sched.start()
