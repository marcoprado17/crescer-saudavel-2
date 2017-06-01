import json

from components.forms import NewsletterEmailForm
from email_blueprint import email_blueprint
from models.newsletter_emails import NewsletterEmails


@email_blueprint.route("/registrar-novo-email-do-newsletter", methods=["POST"])
def register_new_newsletter_email():
    newsletter_email_form = NewsletterEmailForm()
    if newsletter_email_form.validate_on_submit():
        newsletter_emails = NewsletterEmails.get()
        newsletter_emails.add(newsletter_email_form.email.data)
        return "", 200
    else:
        return json.dumps(dict(errors=newsletter_email_form.errors)), 400
