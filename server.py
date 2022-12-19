from flask import Flask, render_template

app = Flask(__name__)

nav = [
    { "title": "Главная", "URL": "/" },  
    { "title": "Звания", "URL": "/ranks" },
    { "title": "Роли в игре", "URL": "/roles" },
    { "title": "Глоссарий", "URL": "/glossary" },
    { "title": "Обо мне", "URL": "/about" },
]

@app.context_processor
def global_context():
    return {
        "nav": nav
    }

@app.route("/")
def hello_world():
    return render_template("index.html", name="Главная")

@app.route("/ranks")
def ranks_view():
    return render_template("ranks.html", name="Звания")

@app.route("/roles")
def roles_view():
    return render_template("roles.html", name="Роли в игре")

@app.route("/glossary")
def glossary_view():
    return render_template("glossary.html", name="Глоссарий")

@app.route("/about")
def about_view():
    return render_template("about.html", name="Обо мне")