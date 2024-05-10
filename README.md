# Passify

## Abstract

Passify is a password manager backend designed to securely manage and store passwords.

## Features

- **Email and Password Authentication**: Enabling secure user login using email and password credentials.
- **JWT Authorization**: Authorizing users with JSON Web Tokens (JWT) for secure access control.
- **New Sign-In Email Notifications**: Sending email alerts when a new sign-in is detected for enhanced security.
- **Device Type Detection**: Identifying device types during new sign-ins to enhance security measures.
- **Password Update Reminders**: Notifying users via email every three months to update their master password.
- **RESTful API Endpoints**: Providing RESTful API endpoints for seamless integration with other applications.
- **Browsable API**: Offering an interactive web interface for exploring the API, making testing and development easier.
- **API Rate Limiting**: Managing API usage to prevent abuse and optimize server performance.
- **Secure Storage**: Encrypting and storing all passwords securely for maximum protection.
- **Admin Panel**: Providing an interface for managing users through Django's admin panel.
- **Automated Tests**: Employing pytest and other testing libraries for efficient and thorough testing.
- **Performance Tests**: Conducting load testing and other performance assessments to ensure scalability and reliability.
- **Logging**: Saving system logs for monitoring and debugging purposes.
- **Fully Dockerized**: Containerizing the application for consistent and simplified deployment.

## Technologies

- [Python](https://www.python.org/)
- [Django](https://github.com/django/django#django)
- [Django REST Framework](https://github.com/encode/django-rest-framework?tab=readme-ov-file#django-rest-framework)
- [djoser](https://github.com/sunscrapers/djoser?tab=readme-ov-file#djoser)
- [Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt?tab=readme-ov-file#simple-jwt)
- [Django Cryptography](https://github.com/georgemarshall/django-cryptography?tab=readme-ov-file#django-cryptography)
- [Django User Agents](https://github.com/selwin/django-user_agents?tab=readme-ov-file#django-user-agents)
- [pytest](https://github.com/pytest-dev/pytest)
- [Locust](https://github.com/locustio/locust?tab=readme-ov-file#locust)
- [Celery](https://docs.celeryq.dev/en/stable/index.html)
- [Flower](https://github.com/mher/flower?tab=readme-ov-file#flower)
- [RabbitMQ](https://www.rabbitmq.com/)
- [Redis](https://redis.io/)
- [smtp4dev](https://github.com/rnwood/smtp4dev)
- [Docker](https://www.docker.com/)

## Running the Project

### Method 1: Using Docker-Compose

To run the project:

```bash
docker-compose build
```

```bash
docker-compose up -d
```

To stop the project:

```bash
docker-compose down -v
```

### Method 2: Using Python and Docker (Recommended)

An alternative way to run the project:

```bash
pip install -r requirements.txt
```

```bash
pip install -r requirements-dev.txt
```

```bash
python manage.py runproject
```

And to stop the project just hit `ctrl+c`.

## Local Development Links

- Access the root endpoint of the API at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
- Receive emails using smtp4dev's web interface at [http://localhost:5000/](http://localhost:5000/).
- Monitor and manage Celery tasks through Flower's web interface at [http://localhost:5555/](http://localhost:5555/).
- Conduct performance tests using Locust's web interface at [http://localhost:8089/](http://localhost:8089/).
- Manage users through the Django admin panel at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).

**Important Note**: Before running a performance test using Locust, you need to create some dummy users. To do this, you can run the following command:

```bash
python manage.py seed_db
```

**Important Note**: To access the admin panel, you need to create an admin user. To do this, you can run the following command:

```bash
python manage.py createsuperuser
```

## Running Tests

To run all the tests, execute the following command:

```bash
pytest
```

If you want to continuously run the tests as you make changes to the code, you can execute the following command:

```bash
ptw
```
