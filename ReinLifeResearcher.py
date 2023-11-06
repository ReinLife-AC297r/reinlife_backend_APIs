#This package is supposed to be researcher side package. The researchers should communicate with the database using this package.
import json

#The server2firestore.py file is a module that provide helper functions to interact with the database
import server2firestore
from server2firestore import get_answers as get_answers
from server2firestore import list_all_userid as list_all_userid
from server2firestore import notification2db as notification2db


default_inputfile='./experiment_info.json'



def readjson(filename):
    """
    helper function to read a json file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data



def set_experiment(inputfile='./experiment_info.json'):
    """
    function to set the experiment information
    """ 
    
    #read experiment data from user defined input file
    expdata = readjson(inputfile)
    
    #upload data to firestore
    return server2firestore.save_exp_to_firebase(expdata)
    
    
    
def set_questionnaires(inputfile='./questionnaires.json'):
    
    #read questionnaire data from user defined input file
    qdata=readjson(inputfile)
    
   
    #upload data to firestore
    return server2firestore.save_qn_to_firebase(qdata)


    
    
