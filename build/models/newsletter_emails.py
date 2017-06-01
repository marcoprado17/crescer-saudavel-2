# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ======================================================================================================================
# Created at 28/03/17 by Marco Aurélio Prado - marco.pdsv@gmail.com
# ======================================================================================================================
from sqlalchemy.orm.attributes import flag_modified

from proj_exceptions import InconsistentDataBaseError
from proj_extensions import db
from models.base import BaseModel


class NewsletterEmails(BaseModel):
    __tablename__ = "newsletter_emails"

    emails_as_json = db.Column(db.JSON, default={}, nullable=False)

    @staticmethod
    def get():
        newsletter_emails = NewsletterEmails.query.all()
        if len(newsletter_emails) != 1:
            raise InconsistentDataBaseError
        return newsletter_emails[0]

    def add(self, email):
        if not "emails" in self.emails_as_json.keys():
            self.emails_as_json["emails"] = []

        self.emails_as_json["emails"] += [email]

        flag_modified(self, "emails_as_json")
        db.session.add(self)
        db.session.commit()

    def get_all_emails(self):
        if not "emails" in self.emails_as_json.keys():
            return []
        return self.emails_as_json["emails"]
