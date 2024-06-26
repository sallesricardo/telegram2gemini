import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GOOGLE_API_KEY=os.environ.get("SECRET_KEY")
TELEGRAM_TOKEN=os.environ.get("TELEGRAM_TOKEN")
