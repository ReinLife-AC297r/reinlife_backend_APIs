

#This package is supposed to be researcher side package. The researchers should communicate with
import json
import server2firestore

from server2firestore import get_answers as get_answers
from server2firestore import list_all_userid as list_all_userid


default_inputfile='./experiment_info.json'






def readjson(filename):
    """
    helper function to read a json file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# def login():
#     pass






def set_experiment(inputfile='./experiment_info.json'):
    """
    function to set the experiment information
    """ 
    
    #load experiment data from inputfile
    expdata = readjson(inputfile)
    #load experiment id from loginfile
    #myexpid = calc_expid(loginfile)
    
    #This is our current implementation
    return server2firestore.save_exp_to_firebase(expdata)
    
    
    
def set_questionnaires(inputfile='./questionnaires.json'):
    
    #load questionnaire data
    qdata=readjson(inputfile)
    #load experiment id
    #myexpid = calc_expid(loginfile)
    
    #upload expdata to server
    #This is our current implementation
    return server2firestore.save_qn_to_firebase(qdata)


    
    
