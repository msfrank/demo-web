import os

from flask import Flask, request, render_template


def create_app(test_config=None):

    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/')
    def greeting():
        context = {}
        context['date'] = request.date
        context['host'] = request.host
        context['user_agent'] = request.user_agent
        context['forwarded'] = request.headers.get('forwarded')
        context['letter_to_display'] = '???'
        try:
            with open('/letter_to_display', 'r') as f:
                context['letter_to_display'] = f.read().strip()
        except:
            pass
        return render_template('greeting.html', context=context)

    return app
