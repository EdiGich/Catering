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
git clone https://github.com/your-username/catering-website.git
cd catering-website
```

### Create a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
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

## Deployment on Render
1. Push your project to GitHub:
   ```sh
   git add .
   git commit -m "Initial commit for Render deployment"
   git push origin main
   ```
2. Sign in to [Render](https://render.com) and create a new **Web Service**.
3. Connect your repository and configure the service:
   - **Build Command:**
     ```sh
     pip install -r requirements.txt
     python manage.py migrate
     python manage.py collectstatic --noinput
     ```
   - **Start Command:**
     ```sh
     gunicorn main.wsgi:application
     ```
   - **Environment Variables:**
     - `DJANGO_SECRET_KEY` = *your-secret-key*
     - `DEBUG` = `False`
     - `DATABASE_URL` = *your-database-url*
4. Click **Deploy** and wait for the process to complete.

## Connecting the Flutter Admin App
- Update the Flutter app API URLs to:
  ```sh
  https://catering_website.onrender.com/api/
  ```
- Ensure WebSocket configurations are pointing to the deployed server.

## License
This project is open-source under the **MIT License**.

## Author
**Your Name**  
Contact: edwingichira801@gmail.com

