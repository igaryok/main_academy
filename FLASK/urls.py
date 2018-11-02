from app import app, log
from flask import render_template, request, redirect, url_for

import funcs


@app.route("/")
def get_payments():

    return render_template("payments.html", payments=funcs.get_all_payments())


@app.route("/new", methods=["GET", "POST"])
def create_payment():
    if request.method == "GET":
        return render_template("new_payment.html",
                               inputs=("name", "created", "amount", "currency"))
    new = funcs.create_new_payment(request.form)
    return redirect(url_for("get_payments", id=new.id))


@app.route("/filter", methods=["GET", "POST"])
def get_filter():
    if request.method == "POST":
        log.debug("call filter with argument")
        return render_template("filter.html", payments=funcs.get_filtered_payments(request.form))
    log.debug("call filter without arg")
    return render_template("filter.html", payments=funcs.get_all_payments())


@app.route("/api/new", methods=["POST"])
def create_api_payment():
    # json request
    return "in create_api_payment"
