from flask import Flask
from utils import load_candidates, get_all, get_by_pk, get_by_skill

candidates: list = load_candidates()


app = Flask(__name__)

@app.route("/")
def page_index():
    return str(get_all(candidates))

@app.route("/profile/")
def page_profile():
    return "Профиль пользователя"

@app.route("/feed/")
def page_feed():
    return "Лента пользователя"

@app.route("/messages/")
def page_messages():
    return "Сообщения пользователя"

@app.route('/users/<int:uid>')
def profile(uid):
    print(uid)
    print(type(uid))
    return f'<h1>Профиль {uid}</h1>'

@app.route('/catalog/items/<itemid>')
def profile_goods(itemid):
    return f'<h1>Страничка товара {itemid}</h1>'

app.run(host='127.0.0.2', port=80)