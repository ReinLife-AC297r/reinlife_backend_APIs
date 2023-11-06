
# ReinLife_Flask
 backend of ReinLife

 ReinLife is going to be a cross-platform open source mobile Health app and research platform.
 We name the backend as "ReinLife_Flase" but currently we are not using Flask. We are using Google firebase service.
 
 The frontend is written in flutter and can be found at [reinlife_flutter](https://github.com/ReinLife-AC297r/reinlife_flutter).

# Current Workflow
1. Recreate python/anaconda environment using environment.yml
2. `example_researcher_defined_code.ipynb` is a jupyter notebook that contains the example code of of the API should be used. The APIs are in the module `ReinLifeResearcher.py`


## Environment Configuration
<!--
### Create Envionement
 conda activate relearnlife
 conda install flask requests
### Save Env
 conda env export > environment.yml)
-->
### Recreate Env
I am using anaconda to create the environment. Here are the steps to repeat the envionment.
```
conda env create -f environment.yml
conda activate reinlife
```
## files
app.py is the draft of the main app.

changewords.py is a utility script to send new words to the port. The new word is currently hardcoded in this file.
