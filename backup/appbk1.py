from flask import Flask, jsonify,request


app = Flask(__name__)


def get_questions_db(experiment_id):
    """
    get questions from database
    """
    #Below is a dummy return
    #For open text questions, the frontend can ask the user to input a number
    #For rating scale questions, the frontend can be a slider
    #For Multiple Choice questions, the frontend can list the choices as buttons
    myquestionnare=[
            { "questionId":1,
            "questionText": "How many hours did you sleep yesterday?",
            "questionType": "Open Text"
                         },
            { "questionId":2,
              "questionText": "What is your mood today?",
              "questionType": "Rating Scale",
              "minValue": 1,
              "maxValue": 5
            },
            { "questionId":3,
              "questionText": "Have you followed the sleep improving guideline?",
              "questionType": "Multiple Choice",
              "options": ['Yes','No']
            }
            ]
    return myquestionnare

@app.route('/questionnaires/experiment/<int:experiment_id>', methods=['GET'])
def send_questions(experiment_id):
    #get_questions_db:get questions from database. To be implemented
    #myquestinoare is a dictionary
    myquestionnare=get_questions_db(experiment_id)
    return jsonify(myquestionnare)


def save_answers_db(experiment_id,user_id,data):
    """
    save user's answers of questionnares to database
    """
    #Below is a dummy function.
    #Communication with the database need to be implemented
    print(f"Saving Experiment {experiment_id} User {user_id} data to database")
    #------------------------------------------------
    # Save to database here, if success, return True, else return false (replace this with actual database logic).
    try:
        # Your database save logic here.
        # If successful, return True.
        print(data)
        return True
    except Exception as e:
        # If there's an error, return False or an error message.
        print(f"Error saving data: {str(e)}")
        return False
    

@app.route('/questionnaires/experiment/<int:experiment_id>/user/<int:user_id>',methods=['POST'])
def receive_user_answers(experiment_id,user_id):
    """
    receive user's answers to questionares from frontend 
    """
    data = request.json
    #data is converted from json to a python dictionary. 
    #Below is an example showing the format of data
    #------------------------------------------------
    #{
    #"answers": [
    #    {"questionId": 1, "answer": "User's answer 1"},
    #    {"questionId": 2, "answer": "User's answer 2"}
    #]
    #}
    #------------------------------------------------
    
    #save_answers_db:save user answers to database. To be implemented
    save_success=save_answers_db(experiment_id,user_id,data)
    if save_success:
        response = {"message": "User answers received successfully"}
        return jsonify(response), 200
    else:
        response = {"message": "User answers not received successfully"}
        return jsonify(response), 400


def get_experiments_db(experiment_id):
    """
    get experiment infos from databse. To be implemented
    """
    #Below is a dummy return

    #Duration is in days
    myexperimentinfo=[
            {"name": "Experiment 1",
             "Topic": "Improving sleep quality following guided cognitive behavioral therapy",
             "Duration":"10"
            }
            ]


@app.route('/experimentinfo/<int:experiment_id>',methods=['GET'])
def send_experiment_info(experiment_id):
    """
    send experiment info to frontend
    """

    #get_experiments_db: get experiment info from database. To be implemented
    myexpinfo=get_experiments_db(experiment_id) 

    return jsonify(myexpinfo)




if __name__ == '__main__':
    app.run(debug=True)

