from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user

router = Blueprint("router", __name__)


@router.route("/")
def index():
    return render_template("index.html")


@router.route("/auth")
def auth():
    if current_user.is_authenticated:
        return redirect(url_for("router.index"))
    return render_template("auth.html")

