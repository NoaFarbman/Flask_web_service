from consts import FASTEST_ANIMAL_DICT
from flask import Flask
import json
app = Flask(__name__)


@app.route("/")
def fastest_animal():
    json_dict = json.dumps(FASTEST_ANIMAL_DICT)
    return json_dict


if __name__ == '__main__':
    app.run(host="0.0.0.0")