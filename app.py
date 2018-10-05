from flask import Flask, make_response, request, jsonify

PORT = 8000

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

instructions = """Endpoints: {}""".format("".join(endpoints))


@app.route('/')
def say_something():
    return "ACTIVE (hit /instructions)"


@app.route('/ulisse/')
def hello():
    return ulisse


@app.route('/instructions/')
def say_instructions():
    return instructions


@app.route('/greet-user/<string:username>/')
def greet_user(username):
    return "Hi "+username


@app.route('/greet-person/', methods=['GET', 'POST'])
def greet_person():
    if request.method == 'GET':
        response_body = {'response': 'Send a POST request'}
        return make_response(jsonify(response_body), 200)
    elif request.method == 'POST':
        r = request.json
        response_body = {'response': "Hi, "+r['person']}
        return make_response(jsonify(response_body), 200)
    else:
        pass


if __name__ == '__main__':
    app.run(port=PORT, debug=True)
