# MyProject Server

## Overview

MyProject Server is a Django-based web application designed to manage various administrative and user-related operations. It includes modules for admin management, user handling, and basket functionality.

## Features

- User management (registration, login, profile)
- Admin functionality for creating and updating users
- Basket management
- REST API endpoints for various operations
- Uses SQLite for data persistence

## Project Structure

- `admins/`: Handles all admin-related views, models, and templates.
- `baskets/`: Contains basket-related logic and views.
- `users/`: Manages user authentication, profiles, and registration.
- `static/`: Static files such as JavaScript, CSS, and images.
- `templates/`: HTML templates for the application.
- `requirements.txt`: List of dependencies required for the project.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or later
- Virtual environment (recommended)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/myproject-server.git
   cd myproject-server
   ```
   
1. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
    ```

1. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

1. Apply migrations:
    ```bash
    python manage.py migrate
    ```

1. Run the development server:
    ```bash
    python manage.py runserver
    ```
    The server will be running on http://127.0.0.1:8000/.

## Usage

### Admin Panel
Access the admin panel at http://127.0.0.1:8000/admin/ after running the server. Use the default admin credentials or create a new admin user using Django's createsuperuser command:

```bash
python manage.py createsuperuser
```

### API Endpoints
- User registration, login, and profile management endpoints are available at /users/.
- Basket management endpoints are located at /baskets/.
