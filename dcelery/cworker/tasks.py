from celery import shared_task

@shared_task
def task1(name='cworker.tasks.task1'):
	print('Task 1 executed.')
	return 'Done'



@shared_task
def task2():
	print("Task 2 is running")
	return "Task 2 complete"



@shared_task
def task3():
	print("Task 3 is running")
	return "Task 3 complete"



@shared_task
def task4():
	print("Task 4 is running")
	return "Task 4 complete"

