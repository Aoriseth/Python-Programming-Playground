import sched,time

scheduler = sched.scheduler(time.time,time.sleep)

def scheduledFunction():
	print("Doing Something")
	scheduler.enter(1, 1, scheduledFunction)

scheduler.enter(1,1,scheduledFunction)
scheduler.run()