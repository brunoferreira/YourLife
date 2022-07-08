from flask import render_template, session, request
from YourLife import app
from YourLife.model import queries

@app.route("/profile/<username>", methods=['GET', 'POST'])
def profile(username):
    profile_photo = queries.get_profile_photo(username)
    summary = queries.get_summary(username)
    album = queries.get_album_photos(username)
    full_name = queries.get_full_name(username)

    if request.method == 'POST' and request.form['content']:
        queries.add_post(username, request.form['content'])

    posts = queries.get_posts(username)
    return render_template('profilePage.html', profile_photo=profile_photo, summary=summary, album=album, posts=posts, full_name=full_name)