# Django REST Framework Project with Celery and Telegram Bot Integration

A Django project that demonstrates the integration of Django REST Framework, Celery for background tasks, and a Telegram bot.

## Features

- User registration and authentication using JWT
- Celery tasks for sending registration emails
- Telegram bot integration
- RESTful API endpoints
- Django Admin interface

## Prerequisites

- Python 3.8+
- Redis
- Telegram Bot Token (from BotFather)
- SMTP credentials for email sending

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd telegram_celery_intergration
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root with the following variables:
```
DEBUG=False
SECRET_KEY=your-secret-key
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-specific-password
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

## Running the Project

1. Start Redis:
```bash
redis-server
```

2. Start Celery worker:
```bash
celery -A core worker -l info
```

3. Start Django development server:
```bash
python manage.py runserver
```

4. (Optional) Start Telegram bot:
```bash
python manage.py run_telegram_bot
```

## API Documentation

### Authentication Endpoints

#### 1. Register a New User
```bash
curl -X POST http://localhost:8000/api/register/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser4",
    "email": "test4@example.com",
    "password": "testpass123"
  }'
```

Response:
```json
{
  "message": "User registered successfully.",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

#### 2. Obtain JWT Token
```bash
curl -X POST http://localhost:8000/api/token/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "testuser4",
    "password": "testpass123"
  }'
```

Response:
```json
{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

#### 3. Refresh JWT Token
```bash
curl -X POST http://localhost:8000/api/token/refresh/ \
  -H "Content-Type: application/json" \
  -d '{
    "refresh": "your-refresh-token"
  }'
```

### Protected Endpoints

To access protected endpoints, include the JWT token in the Authorization header:
```bash
curl -X GET http://localhost:8000/api/protected/ \
  -H "Authorization: Bearer your-access-token"
```

## Telegram Bot

The Telegram bot can be started using the management command:
```bash
python manage.py run_telegram_bot
```

Available commands:
- `/start` - Start the bot and save your Telegram username

## Celery Tasks

The project includes a Celery task for sending registration emails:
- `send_registration_email` - Sends a welcome email to newly registered users

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 