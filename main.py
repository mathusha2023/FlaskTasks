from flask import Flask, render_template, url_for
from forms.double_protection import DoubleProtectForm
from data import db_session
from add_team import add_team

app = Flask(__name__)
app.config["SECRET_KEY"] = "MySuPeRsEcReTkEy"


@app.route("/<title>")
@app.route("/index/<title>")
def index(title):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def training(prof):
    if "инженер" in prof.lower() or "строитель" in prof.lower():
        return render_template("prof.html", title=prof,
                               prof="Инженерные тренажеры", img=url_for("static", filename="img/spaceship_it.png"))
    else:
        return render_template("prof.html", title=prof,
                               prof="Научные симуляторы", img=url_for("static", filename="img/spaceship_ss.png"))


@app.route("/list_prof/<list_type>")
def list_prof(list_type):
    return render_template("list_prof.html", title="Список профессий", list_type=list_type)


@app.route("/answer")
@app.route("/auto_answer")
def auto_answer():
    form = {"surname": "Kovalev", "name": "Vlad", "education": "highest",
            "profession": "Jack of all trades", "sex": "male", "motivation": "for fun", "ready": True}
    return render_template("auto_answer.html", title="Анкета", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = DoubleProtectForm()
    if form.validate_on_submit():
        print("Submit!")
        return render_template("double_form.html", title="Аварийный доступ",
                               form=form, img=url_for("static", filename="img/emblem.png"))
    else:
        return render_template("double_form.html", title="Аварийный доступ",
                               form=form, img=url_for("static", filename="img/emblem.png"))


@app.route("/distribution")
def distribution():
    sp = ["assd sadads", "sad sdad", "dsfsf df dsffsd", "afdfs dsf dfdf", "dsfksdf sdfksdf"]
    return render_template("distribution.html", distribution=sp)


if __name__ == "__main__":
    db_session.global_init("db/mars_explorer.db")
    add_team()
    app.run("127.0.0.1", 8080)
