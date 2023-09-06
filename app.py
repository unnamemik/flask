from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
from models import Users, db

application = Flask(__name__)
application.secret_key = b'b0ee5a2c6515091072087d57c6693be951cd9fc4629e5e66324c8c33331b5768'
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(application)


@application.route('/')
def index():
    return render_template('index.html')


@application.route('/about/')
def about():
    return render_template('about.html')


@application.route('/careers')
def careers():
    return render_template('careers.html')


@application.route('/contact')
def contact():
    return render_template('contact.html')


@application.route('/register')
def register():
    return render_template('register.html')


@application.route('/wishlist')
def wishlist():
    return render_template('wishlist.html')


@application.route('/jackets')
def jackets():
    return render_template('jackets.html')


@application.route('/shoes')
def shoes():
    return render_template('shoes.html')


@application.route('/clothes')
def clothes():
    return render_template('clothes.html')


@application.errorhandler(400)
def page_not_found(e):
    return render_template('404.html'), 400


@application.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500


@application.cli.command("init-db")
def init_db():
    db.create_all()


@application.route('/profile/', methods=['post', 'get'])
def profile():
    return render_template('profile.html')


@application.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    username = form.username.data
    password = form.password.data
    if request.method == 'POST' and form.validate():
        result = Users.query.filter(Users.username == username).all()
        for user in result:
            if user.username == username and check_password_hash(user.password, password):
                context = {'alert_message': f"Добро пожаловать, {username}!"}
                return render_template('profile.html', form=form, **context)
            else:
                context = {'alert_message': "Welcome!"}
                return render_template('registration.html', form=form, **context)
    return render_template('login.html', form=form)


@application.route('/registration/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    username = form.username.data
    email = form.email.data
    password_hash = generate_password_hash(str(form.password.data))
    birthday = form.birthday.data
    terms = form.terms.data
    if request.method == 'POST' and form.validate():
        if Users.query.filter(Users.username == username).all() or Users.query.filter(Users.email == email).all():
            context = {'alert_message': "Пользователь уже существует!"}
            return render_template('registration.html', form=form, **context)
        else:
            context = {'alert_message': f"Добро пожаловать, {username}!"}
            print(Users.query.filter(Users.username == username).all())
            new_user = Users(username=username, email=email, password=password_hash, birthday=birthday, terms=terms)
            db.session.add(new_user)
            db.session.commit()
            return render_template('profile.html', form=form, **context)
    return render_template('registration.html', form=form)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
