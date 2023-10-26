#The scheduler is a separate program and the flask API here is not for researchers 
#to communicate with the APP but just for scheduling new jobs
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

def my_algorithm():
    print("Running schduler...")

@app.route('/set_question_notification')
def set_question_notification():
    expid = request.form.get('expid')
    message = request.form.get('message')
    questionID = request.form.get('questionID')
  

    interval = request.form.get('interval')   
    def questionnaire_reminder():
        print()
    #add job
    scheduler.add_job(
        mymessage.send_message,
        trigger=DateTrigger(run_date=run_time),
        args=[expid, message, questionID]
    )
    return "Notification for answering questionnaire is set!"

if __name__ == '__main__':
    # Create a Scheduler
    scheduler = BackgroundScheduler()
    scheduler.add_job(my_algorithm, 'interval', seconds=10, id='display_message')
    scheduler.start()

    # Close the Schduler when leaving the program
    try:
        app.run(port=5001)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
