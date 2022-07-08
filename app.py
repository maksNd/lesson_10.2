from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill
from constants import picture_url, picture_sourse

candidates: list = load_candidates()

app = Flask(__name__)


@app.route("/")
def all_candidates():
    return get_all(candidates)


@app.route("/candidates/<pk>")
def candidates_by_pk(pk):
    return f"<img src='({picture_sourse})'>, {get_by_pk(candidates, int(pk))}"

@app.route("/skills/<skill>")
def candidates_by_pk(skill):



# @app.route("/profile/")
# def page_profile():
#     return "Профиль пользователя"
#
# @app.route("/feed/")
# def page_feed():
#     return "Лента пользователя"
#
# @app.route("/messages/")
# def page_messages():
#     return "Сообщения пользователя"
#
#
#
# @app.route('/catalog/items/<itemid>')
# def profile_goods(itemid):
#     return f'<h1>Страничка товара {itemid}</h1>'

app.run(host='127.0.0.2', port=80)
