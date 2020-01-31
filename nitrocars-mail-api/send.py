from flask import *
from flask_mail import *

app = Flask(__name__)

app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = 'salesmafiaonline@gmail.com'
app.config['MAIL_PASSWORD'] = 'azamkhan1730'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

users = [{'name': 'aalam', 'email': 'azamkhanaonla@gmail.com'},
         {'name': 'Ayush', 'email': 'azamkhangreaternoida@javatpoint.com'}]

mail = Mail(app)


@app.route("/sendMail")
def index():
  with mail.connect() as con:
    for user in users:
      message = render_template('email_template.html', name=[user['name']])
      msgs = Message(recipients=[user['email']],
                     html=message,
                     reply_to='hello@nitrocars.in',
                     subject='Your visit for Chevrolet Beat has been scheduled',
                     sender='Nitrocars.in <salesmafiaonline@gmail.com>')
      con.send(msgs)
  return "hello"


if __name__ == "__main__":
  app.run(debug=True)
