from flask import Flask, render_template, url_for

app = Flask(__name__)


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


if __name__ == "__main__":
    app.run("127.0.0.1", 8080)
