# TG_Bot_Boilerplate

This project combines:

- **A Telegram bot** built using `aiogram`
- **A web application** with a React + TypeScript frontend and a FastAPI backend
- **State and cache storage** powered by `Redis`
- **A persistent database** using `PostgreSQL`

The goal is to create a fully functional Telegram bot with:

- A convenient web interface
- A REST API
- A database for storing user data and interactions

## Steps to Deploy

### 1. Create PostgreSQL and Redis Databases

- If you have a blank PostgreSQL instance, you can run the SQL commands from `scripts/postgres/create_db.sql` to create the database, user, and password.

### 2. Provide Credentials

- Add credentials for the database and Redis into the `.env` file.

### 3. Set Up Python Environment

- Create a Python virtual environment and install dependencies:

  ```bash
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
  ```

### 4. Provide Database Details

- Add the database details into the `alembic.ini` file.

### 5. Run Alembic Script

- Run the script `Create_alembic.sh` to initiate Alembic.

### 6. Adjust Alembic Environment

- Adjust the file `infrastructure/migrations/env.py` with the following code:

  ```python
  from infrastructure.database.models import *

  target_metadata = Base.metadata
  ```

### 7. Create and Run Migrations

- Create and run migrations using scripts from the `alembic` folder.

### 8. Populate Database

- Populate the database using SQL scripts from `infrastructure/datafiles`.

### 9. Add Bot ID

- Add the bot ID into the `Users` table. You can first start the bot, get an error that contains the bot ID, and then add this ID into the table.

### 10. Adjust Webapp Frontend

- Adjust the file `webapp_frontend/.env` according to your webapp setup. You should have a valid certificate for SSH.

### 11. Run in Development Environment

- To run everything in the development environment, use `./start_dev.sh`.

### 12. Run in Production

- To run everything in production, use `./prod_deploy.sh` (Docker should be installed).