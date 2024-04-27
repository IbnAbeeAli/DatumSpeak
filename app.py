from dotenv import load_dotenv
import os

load_dotenv()


print(f"{'-'*100}")
print(os.getenv("OPENAI_API_KEY_"))
print(os.getenv("USERNAME"))
