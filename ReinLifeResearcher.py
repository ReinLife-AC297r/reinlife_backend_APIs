

#This package is supposed to be researcher side package. The researchers should communicate with
import json
import requests
import server2firestore

default_loginfile='./loginfile.json'
default_inputfile='./experiment_info.json'

API_URL = 'http://127.0.0.1:5000'


researcher_on_server=True


if researcher_on_server:
    '''
    This part is a lazy way to link function from server2firestore to this module
    The reason we want a seperate server2firestore module is that if in the future we no longer want to give researchers full access to the whole databse, we might want to add another layer.
    '''
    from server2firestore import get_answers as get_answers
    from server2firestore import list_all_userid as list_all_userid

def readjson(filename):
    """
    helper function to read a json file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# def login():
#     pass

def calc_expid(loginfile=default_loginfile):
    '''
    Calculate experiment id
    For now, just read it from file
    '''
    #####################################
    ##deal with expname
    data=readjson(loginfile)
    expname,password=data['expname'],data['password']
    print("loginfilename:",expname,password)
    #This is trying to create a unique id
    myexpid=expname+password
    #####################################
    return myexpid




def set_experiment(inputfile='./experiment_info.json',loginfile=default_loginfile):
    """
    function to set the experiment information
    """ 
    
    #load experiment data
    expdata = readjson(inputfile)
    #load experiment id
    myexpid = calc_expid(loginfile)
    
    if researcher_on_server:
        return server2firestore.save_exp_to_firebase(expdata,myexpid)
    else:
        #upload expdata to server
        return upload_data(API_URL+"/set_experiment",expdata,myexpid)
    
    
def set_questionnaires(inputfile='./questionnaires.json',loginfile=default_loginfile):
    
    #load questionnaire data
    qdata=readjson(inputfile)
    #load experiment id
    myexpid = calc_expid(loginfile)
    
    #upload expdata to server
    if researcher_on_server:
        return server2firestore.save_qn_to_firebase(qdata,myexpid)
    else:
        return upload_data(API_URL+"/set_questionnaires",qdata,myexpid)
    
    

    
    
def upload_data(myroute,mydata, myexpid,loginfile=default_loginfile):
    
    #####################################
    ##deal with expname
    data=readjson(loginfile)
    expname,password=data['expname'],data['password']
    print("loginfilename:",expname,password)
    #This is trying to create a unique id
    myexpid=expname+password
    #####################################
    
    headers = {
        'Content-Type': 'application/json',  # Specify that we are sending JSON data
        'Expid': myexpid,
        # You can add other headers here, like authentication details if needed
        # "Authorization": f"Bearer {your_token}"
    }
    
    
    # Convert data into a JSON string
    data_as_json = json.dumps(mydata)
    
    # Send a POST request
    response = requests.post(myroute, headers=headers, data=data_as_json)

    # If needed, you can check the response status code and content
    if response.status_code == 200:
        return response.json()  # Parse and return the JSON response if the server returns one
    else:
        return f"Error {response.status_code}: {response.text}"

    