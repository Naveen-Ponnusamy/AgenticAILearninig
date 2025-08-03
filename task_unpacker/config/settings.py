import os
from dotenv import load_dotenv

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "..", "uploads")
SESSION_DIR = os.path.join(BASE_DIR, "..", "sessions")
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(SESSION_DIR, exist_ok=True)

# Load from .env file
load_dotenv()

# 🔐 API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# 🤖 LLM Model
DEFAULT_MODEL = "gpt-4o"  # Or "gpt-3.5-turbo" for cost-saving

# 🛠️ Feature Flags
DEBUG = True
LOGGING_ENABLED = False  # Set to True if you want log file support later

# 📁 Directories
UPLOAD_DIR = "data/uploads"
RESULT_DIR = "output/results"

SESSION_DIR = os.path.join("data", "sessions")

