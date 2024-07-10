# TG_Bot_Boilerplate

Steps to deploy:

1) Create postgres DB and ReddisDB

If you have blank postgres instance you can ran SQL commands from  scripts/postgres/create_db.sql in order to create DB and user/password

2) Provide credentials for DB and for Reddis into .env file

3) Create python virtual environment and install dependencies:
    
    virtualenv venv

    source venv/bin/activate

    pip install -r requirements.txt

4) provide DB details into file alembic.ini

5) Run script "Create_alembic.sh" to initiate alembic:

6) Adjust file infrastructure/env.py with the floowing code: 

    from infrastructure.database.models import *

    row25: target_metadata = Base.metadata
P
7) Create and run migrations using scripts from alembic folder

8) Populate DB using SQL scripts from infrastructure/datafiles

9) Add the bot ID into table "Users". You can firstly start bot, get an error which contains bot id and after add this id into this table


