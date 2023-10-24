import os

APP_ENV = os.getenv("APP_ENV") if os.getenv("APP_ENV") else "dev"
