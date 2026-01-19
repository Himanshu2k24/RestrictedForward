from flask import Flask
import threading
import bot   # this imports bot.py

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is alive"

def start_bot():
    bot.main()   # your bot start function

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()
    app.run(host="0.0.0.0", port=10000)
