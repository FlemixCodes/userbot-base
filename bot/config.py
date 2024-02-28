import os
from dotenv import load_dotenv

# Загрузка .env файла
load_dotenv()

# Токен пользователя
TOKEN = os.getenv("TOKEN")

# Токены пользователей (Для запуска мультибота, любой итерируемый объект)
TOKENS = ...

# Эмодзи
EMOJI = {
    "watch": "⌚",
    "ok": "✅",
    "user":  "👤",
    "image": "🖼"
}
