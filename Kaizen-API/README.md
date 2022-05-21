# Kaizen API

## Requirements
* Python 3.8.10
* pip3

### Please Note: It is highly encouraged to continue the development process in a Virtual Env

### To setup local development environment,
1. Create a virtual environment
   1. To create virtual env: `python -m virtualenv venv`
   2. To change dir to Scripts: `cd venv/Scripts`
   3. To activate virtual env: `activate`
   4. After the 3rd step you your CLI prompt should changed to **(venv) C:...**
   5. Move back to root folder: `cd ../..`
2. Install all the packages using requirements.txt
   1. `pip install -r requirements.txt `
3. Setup env variables to virtual env (!!!IMPORTANT STEP!!!)
   1. `set FLASK_ENV=development`
   2. `set FLASK_APP=src`
   3. `set PYTHONDONTWRITEBYTECODE=1`

### To run the application: `flask run`

### To freeze your pip packages in to requirements.txt file: 
* `pip freeze > requirements.txt`
  
* Only issue the above freeze command, if you are working in a virtual env or your global pip list does not contains any other unnecessary pip packages.
