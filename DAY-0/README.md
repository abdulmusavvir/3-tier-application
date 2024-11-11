# Simple User Application

This project is a basic three-tier application with a **frontend**, **backend**, and **database**. It allows users to add and view a list of users with their name and email.

## Features

- **View User List**: Displays a list of users fetched from the database.
- **Add User**: Allows adding a user by entering a name and email.

## Technologies Used

- **Frontend**: HTML and JavaScript for user interaction and data submission.
- **Backend**: Flask REST API for handling requests.
- **Database**: MySQL for storing user data with fields for name and email.

## Application Structure

```plaintext
application
├── backend/
│   ├── app.py               # Flask application code
├── frontend/
│   ├── index.html           # HTML for frontend UI
└── database/
    ├── init.sql             # SQL file for database initialization


## Command to run frontend code on the local machine

python3 -m http.server <port on which we want to execute the frontend code>

## command to run backend code on the local machine

pip install -r requirements.txt
python app.py
