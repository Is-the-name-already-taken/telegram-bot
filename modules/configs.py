import os

ENV = os.getenv("APP_ENV", "DEV")
if ENV == "DEV":
    from dotenv import load_dotenv

    load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
ALLOWED_USERS = [int(user) for user in os.getenv("ALLOWED_USERS").split(",")]

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN is not set in environment variables.")


if __name__ == "__main__":
    pass
