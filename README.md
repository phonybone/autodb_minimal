# Minimal autodb REST API server & deployment
Clone/fork this repo to quickly start up a new autodb-based REST API

## Setup
git clone <this repo> <new folder>  
create new (empty) repo in github or gitlab with name of new project  
cd $NEW_PROJECT_NAME  
git remote set-url origin $(git r-url | sed s/autodb_minimal/$NEW_PROJECT_NAME/)  
git push -u origin master  

## Create virtualenv
Use your method of choice.  
source venv/bin/activate (or equivalent)  
pip install -r requirements.txt  

## Create new db with alembic
alembic revision -m '<create new table(s)>'  
<populate database however you need>

## Run
scripts/run_local.sh  
http://localhost:5000 should show swagger page

## Refs
https://stackoverflow.com/questions/22767617/copy-fork-a-git-repo-on-github-into-same-organization
