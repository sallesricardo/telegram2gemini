import numpy as np
import pandas as pd

import google.generativeai as genai

from settings import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

for m in genai.list_models():
  if 'embedContent' in m.supported_generation_methods:
    print(m.name)
