import os
from dotenv import load_dotenv


# загружает переменные окружения из файла *.env
load_dotenv("./app11/local.env")


# logger settings
LOG_DIR = os.environ.get("LOG_DIR")
LOG_FILE = os.environ.get("LOG_FILE")


# root_path --> FastAPI(root_path=OPEN_API_PREFIX)
OPEN_API_PREFIX = os.environ.get("OPEN_API_PREFIX")


# настройки для базы данных
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")


# DATABASE_URL=postgresql+psycopg2://postgres:password@192.168.1.73:7011/post_db
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


# настройки для CELERY
CELERY_BROKER_URL = os.environ.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND")
