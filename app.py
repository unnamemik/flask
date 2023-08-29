from flask import Flask, render_template

application = Flask(__name__)


@application.route('/')
@application.route('/<string:page_name>')
def index(page_name='index.html'):
    return render_template(page_name)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
