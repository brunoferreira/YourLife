from flask import render_template, session
from YourLife import app
from YourLife.model import queries

@app.route("/profile/<username>")
def profile(username):
    profile_photo = queries.get_profile_photo(username)
    summary = queries.get_summary(username)
    album = queries.get_album_photos(username)
    posts = queries.get_posts(username)
    full_name = queries.get_full_name(username)

    return render_template('profilePage.html', profile_photo=profile_photo, summary=summary, album=album, posts=posts, full_name=full_name)