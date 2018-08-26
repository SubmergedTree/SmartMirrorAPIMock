from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import secure_filename


app = Flask(__name__)
CORS(app)
port = 4000
host = '0.0.0.0'


def main():
    app.run(host=host, port=port, debug=True)


@app.route('/status', methods=["GET"])
def status():
    return jsonify({"status": "up"})


@app.route('/getUsers', methods=["GET"])
def getUsers():
    return jsonify([{"name": "Smith",
                     "prename": "John",
                      "username": "jsmith"
                     },
                    {"name": "Max",
                     "prename": "Mustermann",
                     "username": "mMustermann"
                     }
                    ])


@app.route('/getWidgetsOfUser', methods=["GET"])
def getWidgetsOfUser(username):
    if username == "jsmith":
        return jsonify([
            {
                "position": 1,
                "widget": "catFacts",
                "context": ""
            },
            {
                "position": 3,
                "widget": "weatherToday",
                "context": "&units=metric&q=Karlsruhe"
            }
        ])
    elif username == "mMustermann":
        return jsonify([
            {
                "position": 1,
                "widget": "publicHoliday",
                "context": "2018;BW"

            },
            {
                "position": 2,
                "widget": "catFacts",
                "context": ""

            },
            {
                "position": 3,
                "widget": "note",
                "context": "blablabla"

            },
            {
                "position": 4,
                "widget": "chuckNorisJoke",
                "context": ""

            }
        ])
    else:
        return "no widget found"


@app.route('/addPictures', methods=["POST"])
def addPictures():
    number_of = int(request.form['numberOf'])
    username = request.form['username']
    print(username)
    print(number_of)
    for x in range(1, number_of + 1):
        save_image(request.files[str(x)], '', str(x))

    return "Pictures successfully added", 201


def save_image(img, directory, name):
    path = secure_filename(name)
    path = directory + '/' + path
    img.save(name)
    return path


if __name__ == "__main__":
    main()