Library Management System

A Django-based Library Management System that enables admins and students to manage books, issue records, and student registrations efficiently.

Features

Admin panel to manage books and students

Student registration and login

Issue and return book functionality


Unit test coverage

Technologies Used

Python 3.x


Clone the Repository

git clone https://github.com/your-username/LibraryManagementSystem.git
cd LibraryManagementSystem

Create Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`






Run Server

python -m library.main



Running Tests

 python -m unittest tests.test_library

Directory Structure

LibraryManagementSystem/
├── library/              # Main app
│   ├── models.py         # Data models
│   ├── forms.py          # Forms
│   ├── views.py          # Views
│   ├── urls.py           # URL routing
│   └── tests.py          # Basic tests
├── LibraryManagementSystem/
│   ├── settings.py       # Project settings
│   └── urls.py           # Root URLs
├── manage.py             # Django management
└── test_library.py       # Additional unit tests

License

This project is licensed under the MIT License.

Author

Pranali Kalokhe

Feel free to contribute by opening issues or submitting pull requests!