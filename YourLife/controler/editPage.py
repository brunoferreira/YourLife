from flask import render_template, redirect, session
from YourLife import app
from YourLife.model import queries
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField, MultipleFileField
from wtforms.validators import InputRequired, Email, EqualTo, Length
from YourLife import app, db
from werkzeug.utils import secure_filename
from YourLife.model import tables, queries
import os

class EditForm(FlaskForm):
    summary = StringField('Sumário')
    photo = FileField('Foto de perfil')
    album = MultipleFileField('Carregar novas fotos para o álbum')
    submit = SubmitField('Ok')


@app.route("/edit/<username>", methods=['GET', 'POST'])
def edit(username):
    form = EditForm()
    message = ""

    if form.validate_on_submit():
        summary = form.summary.data
        photo = form.photo.data
        album = form.album.data
        if photo:
            filename = secure_filename(photo.filename)
            filepath = os.path.join(
                app.root_path, 'photos', filename
            )
            queries.change_profile_photo(username, filepath)
            photo.save(filepath)
        if summary:
            queries.change_summary(username, summary)
        if album:
            for pic in album:
                filename = secure_filename(pic.filename)
                filepath = os.path.join(
                    app.root_path, 'photos', filename
                )
                queries.add_album_photo(username, filepath)
                pic.save(filepath)
        form.summary.data = ""
        return redirect('/profile/'+username)

    return render_template('editPage.html', form=form, message=message)