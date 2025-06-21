Blog Platform
=============
A Django-based blogging platform with user registration and social authentication via Google, Facebook, and Twitter.

Features
--------
- User registration with form validation
- Social login with Google, Facebook, Twitter (OAuth2)
- Create, edit, delete blog posts
- Comment on posts
- Automatically assign random images to posts without images (via Unsplash API)
- Responsive UI using Bootstrap 5
- PostgreSQL database backend

Technologies Used
-----------------
- Python 3.12+
- Django 4.2.x
- PostgreSQL
- Django REST Framework
- social-auth-app-django
- Bootstrap 5
- Requests (for Unsplash API)
- Rest API

Setup and Installation
----------------------
1. Clone the repository:
   git clone <repository_url>
   cd blog_project

2. Create and activate a virtual environment:
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Linux/macOS:
   source venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Configure the database and environment variables:
   - Create a PostgreSQL database and user
   - Create a `.env` file in the project root with the following variables:

     DB_NAME=blog_db
     DB_USER=blog_user
     DB_PASSWORD=blog_pass
     DB_HOST=localhost
     DB_PORT=5432
     SECRET_KEY=your_secret_key_here
     DJANGO_DEBUG=False

     SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_client_id
     SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_client_secret
     SOCIAL_AUTH_FACEBOOK_KEY=your_facebook_app_id
     SOCIAL_AUTH_FACEBOOK_SECRET=your_facebook_app_secret
     SOCIAL_AUTH_TWITTER_KEY=your_twitter_consumer_key
     SOCIAL_AUTH_TWITTER_SECRET=your_twitter_consumer_secret

5. Apply migrations:
   python manage.py migrate

6. Run the development server:
   python manage.py runserver

Access the application at http://localhost:8000

Usage
-----
- Register a new account or sign in via Google, Facebook, or Twitter.
- Create new blog posts.
- View, comment on, and manage posts.
- Posts without images get random Unsplash images assigned automatically.

Security Notes
--------------
- Make sure to set DJANGO_DEBUG=False in production.
- Use HTTPS in production environments.
- Keep all secret keys and API keys secure in the `.env` file.
- Regularly update dependencies and audit for vulnerabilities.

Deployment
----------
- Recommended to deploy using Docker or on a platform supporting Django apps.
- Configure environment variables appropriately on the server.
- Use a secure database connection.
- Set up HTTPS and security middleware.

Contact
-------
For questions or support, contact: mikail@example.com
