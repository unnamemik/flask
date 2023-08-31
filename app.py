from flask import Flask, render_template, request, redirect, url_for, make_response, session

application = Flask(__name__)
application.secret_key = b'b0ee5a2c6515091072087d57c6693be951cd9fc4629e5e66324c8c33331b5768'


@application.route('/')
@application.route('/<string:page_name>')
def index(page_name='index.html'):
    return render_template(page_name)


@application.route('/mail/')
def mail_get():
    return render_template('mail.html')


@application.post('/login/')
def login():
    name = request.form.get('name')
    mail = request.form.get('mail')
    response = make_response(redirect(url_for('redirectpage', name=name)))
    response.set_cookie(name, mail)
    return response


@application.post('/logout/')
def logout():
    session.pop('name', None)
    return render_template('mail.html')


@application.route('/redirectpage/<name>/')
def redirectpage(name):
    return render_template('redirectpage.html', name=name)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
