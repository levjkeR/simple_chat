from flask import Blueprint, request, redirect, flash, render_template, url_for
from flask_login import login_user, login_required, logout_user
import re
from .model import User

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.post("/login")
def login():
    username, password = request.form.get("username"), request.form.get("password")
    if not re.match(r"[A-Za-z0-9]{4,15}$", username):
        flash("Your username must be 4-15 characters long, contain letters and numbers", category="log_error")
        return redirect(url_for("router.auth"))
    if not re.match(r"[A-Za-z0-9]{4,20}$", password):
        flash("Your password must be 4-20 characters long, contain letters and numbers", category="log_error")
        return redirect(url_for("router.auth"))
    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        flash('Please check your login details and try again.', category="log_error")
        return redirect(url_for("router.auth"))
    login_user(user)
    return redirect(url_for("router.index"))


@auth.post("/register")
def register():
    username, password = request.form.get("username"), request.form.get("password")
    user = User.query.filter_by(username=username).first()
    if user:
        flash("Username already exists", category="reg_error")
        return redirect(url_for("router.auth"))
    if not re.match(r"[A-Za-z0-9]{4,15}$", username):
        flash("Your username must be 4-15 characters long, contain letters and numbers", category="reg_error")
        return redirect(url_for("router.auth"))
    if not re.match(r"[A-Za-z0-9]{4,20}$", password):
        flash("Your password must be 4-20 characters long, contain letters and numbers", category="reg_error")
        return redirect(url_for("router.auth"))
    user = User(username=username, password=password)
    user.save()
    login_user(user)
    return redirect(url_for("router.index"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("router.index"))
