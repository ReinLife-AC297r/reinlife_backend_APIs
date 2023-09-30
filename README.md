
# flask_reinlife
 backend of ReinLife

 ReinLife is an cross-platform open source mobile Health app and research platform.
 
 The frontend is written in flutter and can be found at XXX.

# A quick start guide
1. Recreate python/conda environment using environment.yml
2. do `python app.py` or `flask run`
3. Optionally, one can run `python changeword.py` to change the word that will be passed to the frontend.


## Environment Configuration
<!--
### Create Envionement
 conda activate relearnlife
 conda install flask requests
### Save Env
 conda env export > environment.yml)
-->
### Recreate Env
 conda env create -f environment.yml
## files
app.py is the draft of the main app.

changewords.py is a utility script to send new words to the port. The new word is currently hardcoded in this file.
