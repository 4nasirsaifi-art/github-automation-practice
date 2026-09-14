import os

api_key = os.getenv("MY_API_KEY", "No Key Found")
print(f"Application Running Successfully!")
print(f"Loaded Secret Key: {api_key}")