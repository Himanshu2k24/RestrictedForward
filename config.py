import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8585005246:AAGVzgp-0Jd2f7p075ILa7CYYwVy1aUtj_w")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "36409891"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "71f620b6c208c382268de45fdc8cc943")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5723551431"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://himanshu12feb2k23:JaU8qjZ53Q8mWbP0@cluster0.keoec.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))

# Database channel ID
DATABASE_CHANNEL = -1003579327325  # Replace with your channel ID
