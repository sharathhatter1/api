import os
from dotenv import load_dotenv

load_dotenv()

print(f"ENV: {os.getenv('ENV')}")
print(f"USERNAME: {os.getenv('USERNAME')}")
print(f"PASSWORD: {os.getenv('PASSWORD')}")
