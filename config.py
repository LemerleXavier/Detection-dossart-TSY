import os
from dotenv import load_dotenv

load_dotenv()

# Email
SENDER_EMAIL = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# SMTP
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

MAX_EMAIL_SIZE = 20 * 1024 * 1024  # 20 Mo pour rester sous la limite Gmail
