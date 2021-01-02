from flask import Blueprint, render_template

bp = Blueprint("site", __name__)

@bp.route("/")
def index():
    return render_template("list.html")

@bp.route("/novo")
def new_credit_card():
    return render_template("new.html")

@bp.route("/cartao-credito")
def detail():
    return render_template("detail.html")
