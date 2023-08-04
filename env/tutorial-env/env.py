import os
from dotenv import load_dotenv

load_dotenv()

print(os.getenv("ALBANERO_AUTH_SERVICE_URI"))