import os
from os.path import join, dirname
from dotenv import load_dotenv
import numpy as np
import pandas as pd
import google.generativeai as genai

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

GOOGLE_API_KEY=os.environ.get("SECRET_KEY")
print(GOOGLE_API_KEY)
genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'embedContent' in m.supported_generation_methods:
    print(m.name)
