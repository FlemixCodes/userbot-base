import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN") # Токен пользователя
TOKENS = os.getenv("TOKENS") # Токены пользователей (Для запуска мультибота)

# Эмодзи
EMOJI = {
    "watch": "⌚",
    "ok": "✅",
    "user":  "👤"
}
