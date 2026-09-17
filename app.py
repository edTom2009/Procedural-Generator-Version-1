# libraries

from flask import Flask, redirect, url_for, render_templete

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("/HTML/Dashboard/index.html")

if __name__ == "__main__":
    app.run()

