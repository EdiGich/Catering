# Catering Website (Django)

This is a **Django-based catering website** that provides an online platform for a catering company to showcase services, manage a gallery, and receive customer inquiries. The site supports **dynamic content management** through an admin Flutter app.

## Features

- **Home Page** – Overview of the catering business.
- **About Page** – Details about the company and its values.
- **Services Page** – Information on corporate catering, social events, and canteen management.
- **Sample Menus** – Example menus offered by the company.
- **Gallery** – Displays images of past catering events.
- **Contact Us** – Form for customers to send inquiries.
- **Admin Content Management** – Allows admins to update content via a Flutter app.
- **WebSocket Notifications** – Sends real-time notifications to the admin app when a new message is received.

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Frontend:** HTML, Bootstrap, CSS
- **Database:** PostgreSQL (or SQLite for local development)
- **Authentication:** Django authentication system
- **Hosting:** Render
- **WebSockets:** Django Channels for real-time notifications

## Installation & Setup

### Prerequisites

Ensure you have the following installed:

- Python 3
- Pip
- Virtualenv

### Clone the Repository

```sh
git clone https://github.com/edigich/catering.git
cd catering_website
```

### Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate
# On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Apply Migrations

```sh
python manage.py migrate
```

### Create a Superuser

```sh
python manage.py createsuperuser
```

### Run the Development Server

```sh
python manage.py runserver
```

### Collect Static Files

```sh
python manage.py collectstatic --noinput
```

## License

This project is open-source under the **MIT License**.

## Author

Edwin
Contact: edwingichira801@gmail.com
