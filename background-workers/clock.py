from apscheduler.schedulers.blocking import BlockingScheduler
import jobs

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='sun', hour=20)
def update_job():
    jobs.get_amazon()

@sched.scheduled_job('cron', day_of_week='sun', hour=20)
def update_job():
    jobs.get_costco()

@sched.scheduled_job('cron', day_of_week='sun', hour=20)
def update_job():
    jobs.get_walmart()

@sched.scheduled_job('cron', day_of_week='sun', hour=21)
def update_job():
    jobs.update_database()

sched.start()
