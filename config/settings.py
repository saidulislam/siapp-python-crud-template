DEBUG = True

SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'generateastrong128chartoken'

# Flask-Mail.
MAIL_DEFAULT_SENDER = 'contact@local.host'
MAIL_SERVER = 'smtp.mailtrap.io'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'asdf'
MAIL_PASSWORD = 'asdf'

# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5
