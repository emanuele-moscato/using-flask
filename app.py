from flask import Flask, make_response, request, jsonify, url_for, \
    redirect, abort, render_template
import logging
import daiquiri
import sys
import os

PORT = 8000
LOGS_DIR = './logs/'

if not os.path.isdir(LOGS_DIR):
    os.mkdir(LOGS_DIR)

daiquiri.setup(
    level=logging.INFO,
    outputs=(
        daiquiri.output.Stream(sys.stdout),
        daiquiri.output.File(
            os.path.join(LOGS_DIR, 'api_logs.log'),
            formatter=daiquiri.formatter.TEXT_FORMATTER
        )
    )
)

logger = daiquiri.getLogger(__name__)

app = Flask(__name__)

ulisse = """Nella mia giovinezza ho navigato
lungo le coste dalmate. Isolotti
a fior d'onda emergevano, ove raro
un uccello sostava intento a prede,
coperti d'alghe, scivolosi, al sole,
belli come smeraldi. Quando l'alta
marea e la notte li annullava, vele
sottovento sbandavano più al largo,
per sfuggirne l'insidia. Oggi il mio regno
è quella terra di nessuno. Il porto
accende ad altri i suoi lumi; me al largo
sospinge ancora il non domato spirito,
e della vita il doloroso amore."""

endpoints = ['/', '/ulisse/', '/instructions/', '/greet-user/<username>/']

instructions = "Hit other endpoints."


@app.route('/')
def say_something():
    return redirect(url_for('say_instructions'))


@app.route('/ulisse/')
def hello():
    return ulisse


@app.route('/instructions/')
def say_instructions():
    return instructions


@app.route("/abort/")
def abort_endpoint():
    abort(401)


@app.route('/greet-user/')
@app.route('/greet-user/<string:username>/')
def greet_user(username=None):
    if username:
        return "Hi "+username
    else:
        return "Hi"


@app.route('/greet-person/', methods=['GET', 'POST'])
def greet_person():
    if request.method == 'GET':
        response_body = {
            'url': url_for('greet_person'),
            'response': 'Send a POST request'
        }
        return make_response(jsonify(response_body), 200)
    elif request.method == 'POST':
        r = request.json
        response_body = {
            'url': url_for('greet_person'),
            'response': "Hi, "+r['person']
        }
        return make_response(jsonify(response_body), 200)
    else:
        pass


@app.route('/index/')
def render_index():
    return render_template('index.html')


if __name__ == '__main__':
    try:
        app.run(port=PORT, debug=True)
    except Exception:
        logger.error("Error executing main routine", exc_info=True)
