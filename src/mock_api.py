from flask import Flask, jsonify, request


app = Flask(__name__)
port = 4000
host = '0.0.0.0'


def main():
    app.run(host=host, port=port, debug=True)


@app.route('/status', methods=["GET"])
def status():
    return jsonify({"status": "up"})


if __name__ == "__main__":
    main()