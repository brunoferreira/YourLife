from flask import render_template, session
from YourLife import app
from YourLife.model import queries

@app.route("/profile/<username>")
def profile(username):
    if username == session['username']:
        return render_template('profilePage.html')
    else:
        return render_template('profilePage.html')