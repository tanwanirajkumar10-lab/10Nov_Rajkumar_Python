# PythonAnywhere Deployment Guide for WriteSphere

Follow these steps to deploy WriteSphere to PythonAnywhere:

## 1. Source Code and Virtual Environment Setup
1. Open a Bash console on PythonAnywhere.
2. Clone your repository:
   ```bash
   git clone <your-github-repo-url> writesphere
   cd writesphere
   ```
3. Create a virtual environment:
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 2. Environment Variables (.env)
1. Create a `.env` file in the project root on PythonAnywhere:
   ```bash
   nano .env
   ```
2. Add your production secrets:
   ```env
   SECRET_KEY=your_production_secret_key_here
   DEBUG=False
   DB_NAME=your_pythonanywhere_username$module_4
   DB_USER=your_pythonanywhere_username
   DB_PASSWORD=your_mysql_password
   DB_HOST=your_pythonanywhere_username.mysql.pythonanywhere-services.com
   DB_PORT=3306
   ```

## 3. Database Setup
1. Go to the **Databases** tab in PythonAnywhere and initialize your MySQL password.
2. Create a database named `module_4`.
3. Go back to your Bash console and run migrations:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

## 4. Static and Media Files
1. Run collectstatic to gather all static files for deployment:
   ```bash
   python manage.py collectstatic
   ```

## 5. Web App Configuration
1. Go to the **Web** tab in PythonAnywhere.
2. Click **Add a new web app**, choose **Manual configuration**, and select **Python 3.10**.
3. In the **Virtualenv** section, enter the path to your virtual environment (e.g., `/home/yourusername/.virtualenvs/myenv`).
4. In the **Code** section, set the **Source code** directory to `/home/yourusername/writesphere`.
5. Open the **WSGI configuration file** linked in the Web tab and edit it to point to your project:

   ```python
   import os
   import sys

   path = '/home/yourusername/writesphere'
   if path not in sys.path:
       sys.path.append(path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'Module_4.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

6. In the **Static files** section of the Web tab, map:
   - URL `/static/` to `/home/yourusername/writesphere/staticfiles`
   - URL `/media/` to `/home/yourusername/writesphere/media`

7. Click **Reload** at the top of the Web app configuration page. Your app should now be live!
