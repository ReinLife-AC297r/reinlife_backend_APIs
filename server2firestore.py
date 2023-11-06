import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
#cred = credentials.Certificate("./reinlife-915bd-firebase-adminsdk-hydd2-96cf9b9942.json")

cred = credentials.Certificate("./flutternotification-ebd50-firebase-adminsdk-dum2k-315e67534e.json")
firebase_admin.initialize_app(cred)
db = firestore.client()




def save_exp_to_firebase(data):
    """
    server side code: save experiment info to firebase
    data is a json file
    """
    # add to collection "Experiments" in firestore
    experiments_ref = db.collection('Experiment Information')
    experiments_ref.document('Experiment Information').set(data)
    return 

def save_qn_to_firebase(data):
    """
    server side code: save questionnaire info to firebase
    data is a json file
    """
    #add to subcollection "Questionnaires" in firestore
    questionnaires_ref=db.collection('Questionnaires')
    for questionnaire_name, questions in data.items():
        doc_ref = questionnaires_ref.document(questionnaire_name)
        doc_ref.set({"questions": questions})   
    return


def get_answers(Userid,option='latest'):
    """
    get answers of a User under an Experiment
    
    answers is a dictionary or a json file
    
    In this current version, we choose to only output answers field, 
    but ignore other fields like timestamp questionnaire ID
    """
    
    exp_ref = db
        
    users_with_specific_uid = exp_ref.collection('Users').document(Userid)
    if option=='all':
        print(f"get User:{Userid} answers: all")
        answers = users_with_specific_uid.collection('user answers').stream()
        myanswers=[answer_doc.to_dict()['answers'] for answer_doc in answers]
        for answer in myanswers:
            print(answer)
    elif option=='latest':
        print(f"get User:{Userid} answers: latest")
        latest_answer = users_with_specific_uid.collection('user answers').order_by('time', direction=firestore.Query.DESCENDING).limit(1).stream()
        
        for answer_doc in latest_answer:
            #print("now in loop")
            myanswers = answer_doc.to_dict()['answers']
            print(myanswers)
    else:
        print("else")
        raise NotImplementedError("To be implemented")
       
    return myanswers

def list_all_userid():
    """
    get answers of a User under an Experiment
    
    answers is a dictionary or a json file
    """
   

    exp_ref = db

    users_subcollection_docs = exp_ref.collection('Users').stream()
   
    doc_ids = [doc.id for doc in users_subcollection_docs]

    print(doc_ids)
    return doc_ids

