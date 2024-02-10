# ENGO551_Lab1

Overview
This project involved creating a Flask web application allows users to register, log in, search for books, and leave reviews for individual books. It also includes functionality to prevent a user from submitting multiple reviews for the same book, enhancing the integrity of the review data.

Project Structure
application.py: The main Flask application file containing route definitions for the website. This includes routes for user registration, login, book search, and review submission.

requirements.txt: Lists all Python packages that need to be installed to run the application.

import.py: A separate script for importing book data from a CSV file into the PostgreSQL database.

templates/: This directory contains HTML files for the application's frontend.

base.html: The base template that includes the navigation bar and the structure for flash messages. Other templates extend this base.
index.html: The landing page template, offering options to log in or register.
login.html: The login page template.
register.html: The registration page template.
home.html: The home page template displayed after a user logs in.
search.html: The template for searching books.
search_results.html: Displays search results.
book_page.html: Displays book details and allows users to submit reviews.

Additional Information
The project uses PostgreSQL for the database back-end.
User passwords are hashed for security using Werkzeug's generate_password_hash and check_password_hash.
SQLAlchemy is used for database interaction.
Flash messages are used to provide feedback to the user.
