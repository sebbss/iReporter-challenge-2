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

## Endpoints
|HTTP Method | End point | Action|
|-------|---------|----------|
| POST | /ireporter/api/v1/flag | create a red-flag |
| GET | /ireporter/api/v1/flags | get all red-flags |
| GET | /ireporter/api/v1/flags/<int:flag_id> | get a specific red-flag |
| DELETE | /ireporter/api/v1/flags/<int:flag_id> | delete a specific red-flag |
| PATCH | /ireporter/api/v1/flags/<int:flag_id>/description | update the description of a red-flag |
| PATCH | /ireporter/api/v1/flags/<int:flag_id>/location | update the location of a red-flag |

## Built with 
- Flask [python framework]
- Pytest [testing framework]
 
## Author
-Senabulya Joseph