from flask import Blueprint, render_template

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/lista")
def list_credit_card():
    return render_template("list.html")


@bp.route("/cartao-credito")
def detail():
    return render_template("detail.html")
