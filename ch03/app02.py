import random
from flask import Flask
app = Flask(__name__)

surname = "Witowski"

@app.route("/")
def home():
    name = "Sebastian"
    lucky = random.randint(0, 100)

    return f"Hello {name}! Your lucky number is: {lucky}."
