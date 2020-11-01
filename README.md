## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
Password_Checker is a small python tool for identifying passwords that previously been hacked.
	
## Technologies
Project is created with:
* Python3
* haveibeenpwned V3 API
* SHA1 hashing
* configparser - for config.ini file
	
## Setup
* Clone this repository to your local environment.
* Open ./config/config.ini and enter all your password under the 'password' field.
* open any shell and run:
    ````
      $python checkmypass.py
    ````
