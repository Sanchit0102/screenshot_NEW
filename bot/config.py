import os


class Config:

    API_ID = int(os.environ.get("API_ID", "11615722"))
    API_HASH = os.environ.get("API_HASH", "c992746520e8886d3330de2ec9a1a3a7")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5655590355:AAGJu4JlThJ4WXOxpclgnJKH351xgZJiYYc")
    SESSION_NAME = os.environ.get("SESSION_NAME", "@screenshot2_bot")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001898159090"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://scre:scre@cluster0.yzmsx7i.mongodb.net/?retryWrites=true&w=majority")
    AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "5596825598").split(" ")]
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", False))
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 5))
    HOST = os.environ.get("HOST", "")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
