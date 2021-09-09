import flask
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

# If in case API fails, fallback data
videosFixtures = [
    "https://www.youtube.com/watch?v=ASukJ7_3k4A",
    "https://www.youtube.com/watch?v=lOqSQgHUWW4",
    "https://www.youtube.com/watch?v=qqZ_SH9N3Xo&t=1s",
    "https://www.youtube.com/watch?v=uDmSZX_zVuQ",
    "https://www.youtube.com/watch?v=EdDeNih73eI"
]

@app.route('/', methods=['GET'])
def home():
    return '''PING PONG!!'''

@app.route('/api/videos', methods=['GET'])
def videos():
    return jsonify(videosFixtures)

app.run()