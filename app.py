#========Imports========
from flask import Flask, redirect, request, flash
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
#from terrain import generate_terrain

#========Flask app setup========
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key in production

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

#========Database setup========
db = SQLAlchemy(app)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

#========Render templates========
@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route("/register", methods=['GET', 'POST'])
def register():
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

#========form handling========
#new user registration
@app.route('/add', methods=["POST"])
def profile():
    username = request.form.get("username")
    password = request.form.get("password")


    if not User.query.filter_by(username=username).first():  # Check if user already exists
        u = User(username=username, password=password)
        db.session.add(u)
        db.session.commit()
        return redirect('/login')
    else:
        flash("Username already exists. Please choose a different one.")
        return redirect('/register')
  

#login check
@app.route('/loginCheck', methods=['POST'])
def loginCheck():
    username = request.form.get("username")
    password = request.form.get("password")

    user = User.query.filter_by(username=username, password=password).first()

    if user:
        return redirect('/dashboard')
    else:
        flash("Invalid username or password. Please try again.")
        return redirect('/login')  # Redirect back to login on failure

#terrain generation route
@app.route("/generate", methods=["POST"])
def generate():
    width = int(request.form["mapWidth"])
    height = int(request.form["mapHeight"])
    seed = float(request.form["seedVal"])
    detail = float(request.form["detailVal"])

    generate_terrain(width, height, seed, detail)

    return "Terrain generated successfully!"




      
if __name__ == '__main__':
    with app.app_context():  # Needed for DB operations
        db.create_all()      # Creates the database and tables
    app.run(debug=True)