import schedule
import time

def my_task():
    print("Task executed!")

# Schedule the task
schedule.every(2).seconds.do(my_task)

# Run the pending tasks in a loop for a fixed number of times

schedule.run_pending()

