# ArciTech-Assignment

## Project Overview

ArciTech Assignment is a web application developed using Django and Python. The goal of the project is to create a robust web solution that focuses on user authentication, content management system, and providing a RESTful API for interaction.

## Features

- **User Authentication**: Sign up, log in, and manage user profiles.
- **Content Management**: Create and manage content with the option to update or delete them.
- **RESTful API**: Expose endpoints to interact with the backend data, such as managing users and projects.

## Technologies Used

This project utilizes the following technologies:

- **Python**: Backend development language used for the application's core functionality.
- **Django**: Web framework used for rapid development of the web application.
- **SQLite**: Default database for development, can be easily swapped with other databases.
- **Django REST Framework**: Toolkit for building Web APIs to handle user and project data interactions.
- **Git**: Version control system for source code management.

## Getting Started

### Prerequisites

1. Python 3.8+ installed.
2. Virtualenv for creating isolated environments.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Roshancode99/ArciTech-Assignment.git
    cd ArciTech-Assignment
    ```

2. Create a virtual environment:
    ```bash
    virtualenv workenv
    source workenv/bin/activate  # On Windows, use workenv\Scripts\activate
    ```

3. Install the required dependencies:
    pip install django and other dependencies

### Running the Application

1. Apply the migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

2. Run the development server:
    ```bash
    python manage.py runserver
    ```

3. Open your browser and go to `http://127.0.0.1:8000/` to access the application.



