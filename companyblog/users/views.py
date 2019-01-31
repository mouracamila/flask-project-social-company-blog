#users/views.py
from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import db
from companyblog.models import User, BlogPost
from companyblog.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)


# register
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.emal.data,
                    username = form.username.data,
                    password = form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Thanks for registration!')
        return redirect(url_for('users.login'))

    return render_template('register.html',form=form)

# login



# logout
@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("core.index"))

# account (update UserForm)
# user's list of Blog posts