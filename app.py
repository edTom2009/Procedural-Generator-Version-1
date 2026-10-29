from flask import Flask, render_template, request
from terrain import generate_terrain

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    width = int(request.form["mapWidth"])
    height = int(request.form["mapHeight"])
    seed = float(request.form["seedVal"])
    detail = float(request.form["detailVal"])

    generate_terrain(width, height, seed, detail)

    return "Terrain generated successfully!"


if __name__ == "__main__":
    app.run(debug=True)