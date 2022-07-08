from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill
from constants import picture_url, picture_url_2

candidates: list = load_candidates()

app = Flask(__name__)


@app.route("/")
def all_candidates():
    return get_all(candidates)


@app.route("/candidates/<pk>")
def candidates_by_pk(pk):
    return f"<img src='({picture_url})'>, {get_by_pk(candidates, int(pk))}"


@app.route("/skills/<skill>")
def candidates_by_skill(skill):
    return get_by_skill(candidates, skill)


app.run(host='127.0.0.2', port=80)
