# iReporter
iReporter is a web applcation that enables the public to raise red-flags about corruption situations in their neeighbourhoods and also interven in the re-development of the roads or other infrastrature that has worn out

[![Build Status](https://travis-ci.org/sebbss/iReporter-challenge-2.svg?branch=develop)](https://travis-ci.org/sebbss/iReporter-challenge-2)
[![Coverage Status](https://coveralls.io/repos/github/sebbss/iReporter-challenge-2/badge.svg?branch=coveralls)](https://coveralls.io/github/sebbss/iReporter-challenge-2?branch=coveralls)
[![Maintainability](https://api.codeclimate.com/v1/badges/58e3664e3af045a4cc6f/maintainability)](https://codeclimate.com/github/sebbss/iReporter-challenge-2/maintainability)

## Getting Started
To get the application running you need to clone https://github.com/sebbss/iReporter-challenge-2.git

### Prerequisites
You have to get python 3 and pip installed on your machine

### Installing
Go to where you cloned the web application, create a virtual environment, activate it and install requirements.txt
- ```cd iReporter-challenge-2```
- ```virtual venv```
- ```cd venv```
- ```source venv/bin/activate```
- ```pip install -r requirements.txt```

## Running the tests
to run the automated tests 
- ```cd iReporter-challenge-2```
- ```pytest```

## Features
Users can perform the following tasks
- get all red-flags
- create a red-flag
- get a specific red-flag
- update the location of a red-flag
- update the description of a red-flag
- delete a specific red-flag
- login a user
- register a user
- update status of redflag
- update status of intervention
- get all interventions
- create an intervention
- get a specific intervention
- update the location of an intervention
- update the description of an intervention
- delete a specific intervention


## Endpoints
|HTTP Method | End point | Action|
|-------|---------|----------|
| POST | /ireporter/api/v1/flag | create a red-flag |
| GET | /ireporter/api/v1/flags | get all red-flags |
| GET | /ireporter/api/v1/flags/<int:flag_id> | get a specific red-flag |
| DELETE | /ireporter/api/v1/flags/<int:flag_id> | delete a specific red-flag |
| PATCH | /ireporter/api/v1/flags/<int:flag_id>/description | update the description of a red-flag |
| PATCH | /ireporter/api/v1/flags/<int:flag_id>/location | update the location of a red-flag |
| POST | /register | register a user |
| POST | /login | login a user |
| PATCH | /red_flags/<int:flag_id>/status | update status of a red-flag |
| PATCH | /interventions/<int:flag_id>/status | update status of an intervention |
| POST | /ireporter/api/v2/intervention | create an intervention |
| GET | /ireporter/api/v2/interventions | get all interventions |
| GET | /ireporter/api/v2/intervention/<int:flag_id> | get a specific intervention |
| DELETE | /ireporter/api/v2/intervention/<int:flag_id> | delete an intervention |
| PATCH | /ireporter/api/v2/intervention/<int:flag_id>/description | update an intervention description |
| PATCH | /ireporter/api/v2/intervention/<int:flag_id>/location | update an intervention location |
## Built with 
- Flask [python framework]
- Pytest [testing framework]
 
## Author
-Senabulya Joseph