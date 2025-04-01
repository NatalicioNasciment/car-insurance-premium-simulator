import os
from sqlalchemy.engine.url import URL

DATABASE_CONFIG = {
    "drivername": os.getenv("DB_DRIVER", "postgresql"),
    "username": os.getenv("DB_USER", "user"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "host": os.getenv("DB_HOST", "localhost"),
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "insurance_db"),
}

DATABASE_URL = URL.create(**DATABASE_CONFIG)
