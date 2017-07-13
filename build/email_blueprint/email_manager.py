# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 22/12/16 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from flask import current_app
from flask import render_template
from flask import url_for
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from proj_extensions import mail


class EmailManager(object):
    def send_create_account_confirmation_email(self, receiver_email):
        ts = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        subject = "Crescer Saudável | Confirme seu endereço de e-mail"
        token = ts.dumps(receiver_email, salt=current_app.config["EMAIL_TOKEN_SALT"])
        confirm_url = url_for("user_management.email_confirmed", token=token, _external=True)
        logo_url = url_for("static", filename="imgs/logo.png", _external=True)
        data = dict(
            confirm_url= confirm_url,
            logo_url= logo_url,
            email=receiver_email,
        )
        html = render_template("email/activate_account.html", data=data)
        msg = Message(sender=current_app.config["MAIL_USERNAME"], recipients=[receiver_email], subject=subject, html=html)
        mail.send(msg)

    def send_redefine_password_email(self, receiver_email):
        subject = "Crescer Saudável | Redefinição de senha"
        ts = URLSafeTimedSerializer(current_app.config["SECRET_KEY"])
        token = ts.dumps(receiver_email, salt=current_app.config["EMAIL_TOKEN_SALT"])
        recover_url = url_for("user_management.redefine_password", token=token, _external=True)
        logo_url = url_for("static", filename="imgs/logo.png", _external=True)
        data = dict(
            recover_url=recover_url,
            logo_url=logo_url
        )
        html = render_template("email/redefine_password.html", data=data)
        msg = Message(sender=current_app.config["MAIL_USERNAME"], recipients=[receiver_email], subject=subject, html=html)
        mail.send(msg)

email_manager = EmailManager()
