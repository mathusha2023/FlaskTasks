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


if __name__ == "__main__":
    app.run("127.0.0.1", 8080)
