# test_env.py

import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("GOOGLE_API_KEY"))