from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
	return "bapak zuliar ganteng"

app.run(debug=True)