from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate("./reinlife-915bd-firebase-adminsdk-hydd2-96cf9b9942.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def calc_Expid():
    """
    A function to calculate Experiment ID
    May later be extended to a more complex and securer function
    """
    headers=request.headers
    return headers['Expid']

@app.route('/set_experiment', methods=['POST'])
def set_experiment_firebase():
    print("now, add_experiment")
    #get json data
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Missing JSON data"}), 400
    
    #get experiment id
    Expid=calc_Expid() 
    
    
    print("headers.Expid:",Expid)
    # add to collection "Experiments" in firestore
    experiments_ref = db.collection('Experiments')
    experiments_ref.document(Expid).set(data)

    return jsonify({"msg": "Data added successfully"}), 200

@app.route('/set_questionnaires', methods=['POST'])
def set_questionnaires_firebase():
    data = request.get_json()
    if not data:
        return jsonify({"msg": "Missing JSON data"}), 400
    
    #get experiment id
    Expid=calc_Expid() 
    #add to subcollection "Questionnaires" in firestore
    questionnaires_ref=db.collection('Experiments').document(Expid).collection('Questionnaires')
    
    

    for questionnaire_name, questions in data.items():
        doc_ref = questionnaires_ref.document(questionnaire_name)
        doc_ref.set({"questions": questions})
        
    return jsonify({"msg": "Data added successfully"}), 200
    
    

if __name__ == '__main__':
    app.run(debug=True)
