# daas_py_api_facility
## Project

Refrence of DaaS Project - https://github.com/nealrout/daas_docs

## Description

This is an implementation of Django to expose endpoints for the facility object.  This project will follow the standard
features of Django, such as model, serializer and ModelViewSet.  The daas_py_api_asset is more granular for finer
control of DB layer.

__The Liquibase project containing DB objects:__  
https://github.com/nealrout/daas_db


## Table of Contents

- [Requirements](#requirements)
- [Uninstall-Install](#uninstall-install)
- [Usage](#usage)
- [Package](#package)
- [Features](#features)
- [Miscellaneous](#miscellaneous)
- [Contact](#contact)

## Requirements
__Set .env variables for configuration__  

ENV_FOR_DYNACONF=\<environment\>  
_i.e. development, integration, production_  

DYNACONF_SECRET_KEY=\<secret_key\>

## Uninstall-Install
__Uninstall:__  
python -m pip uninstall daas_py_api_facility

__Install:__  
python -m pip install .

__Rebuild from source:__  
python -m pip install --no-binary :all: .

## Usage
__Set correct directory:__  
cd .\facility_api\  

__Start Django api:__  
python manage.py runserver

## Package
python setup.py sdist

## Features
-

## Miscellaneous

### To create new virtual environment  
python -m venv .venv

### To activate the virtual environment for this project
..\.venv\Scripts\activate

### Django (notes only)
__To create a new bootstrapped projects:__  
django-admin startproject facility_api

cd facility_api  

__To create a new application:__  
python manage.py startapp facility

__To handle DB migrations:__  
python manage.py makemigrations facility
python manage.py migrate

## Contact
Neal Routson  
nroutson@gmail.com