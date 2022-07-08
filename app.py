from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill

if __name__ == "__main__":
    candidates: list = load_candidates()

    app = Flask(__name__)


    @app.route("/")
    def all_candidates() -> str:
        return get_all(candidates)


    @app.route("/candidates/<pk>")
    def candidates_by_pk(pk) -> str:
        return f"{get_by_pk(candidates, int(pk))}"


    @app.route("/skills/<skill>")
    def candidates_by_skill(skill) -> str:
        return get_by_skill(candidates, skill)


    app.run(host='127.0.0.2', port=80)
