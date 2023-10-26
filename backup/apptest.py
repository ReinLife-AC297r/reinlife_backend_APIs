import server2firestore
from flask import Flask, request, jsonify


app = Flask(__name__)

def get_expid():
    """
    A function to get Experiment ID
    May later be extended to a more complex and securer function
    """
    headers=request.headers
    return headers['Expid']

@app.route('/set_experiment', methods=['POST'])
def set_experiment_firebase():
    print("now, add_experiment")
    
    data = request.get_json()
    #get experiment id
    Expid=get_expid()    
    print("headers.Expid:",Expid)
    
    if not data:
        return jsonify({"msg": "Missing JSON data"}), 400
    
    server2firestore.save_exp_to_firebase(data,Expid)

    return jsonify({"msg": "Data added successfully"}), 200

@app.route('/set_questionnaires', methods=['POST'])
def set_questionnaires_firebase():
    #get json data
    data = request.get_json()
    #get experiment id
    Expid=get_expid()
    if not data:
        return jsonify({"msg": "Missing JSON data"}), 400
    
    server2firestore.save_qn_to_firebase(data,Expid)
    
        
    return jsonify({"msg": "Data added successfully"}), 200
    
    

if __name__ == '__main__':
    app.run(debug=True)
