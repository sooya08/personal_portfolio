
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message


app = Flask(__name__)

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "your_secret_key"  # for flash messages

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'sooryas851@gmail.com'   # your Gmail (lowercase better)
app.config['MAIL_PASSWORD'] = 'cvvdmfphurxepcup'       # App Password (remove spaces!)
app.config['MAIL_DEFAULT_SENDER'] = 'sooryas851@gmail.com'

mail = Mail(app)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        try:
            # 📩 Send message to YOU
            msg_to_me = Message(
                subject=f"New message from {name}",
                recipients=["sooryas851@gmail.com"],  # your Gmail
                body=f"From: {name}\nEmail: {email}\n\nMessage:\n{message}"
            )
            mail.send(msg_to_me)

            # 📩 Auto-reply to USER
            msg_to_user = Message(
                subject="Thanks for contacting Soorya!",
                recipients=[email],  # user’s email from form
                body=f"Hi {name},\n\nThanks for reaching out! I have received your message:\n\n\"{message}\"\n\nI’ll get back to you soon.\n\nRegards,\nSoorya J"
            )
            mail.send(msg_to_user)

            flash("✅ Your message has been sent. A confirmation was also sent to your email.", "success")
        except Exception as e:
            flash(f"❌ Failed to send message. Error: {str(e)}", "danger")

        return redirect(url_for("contact"))

    return render_template("contact.html")



# Home Page
@app.route("/")
def home():
    return render_template("index.html")

# Projects Page
@app.route("/projects")
def projects():
    return render_template("projects.html")

# Resume Page
@app.route("/resume")
def resume():
    return render_template("resume.html")

if __name__ == "__main__":
    app.run(debug=True)
