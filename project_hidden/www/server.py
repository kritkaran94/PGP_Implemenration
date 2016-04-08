from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib

import flask

app = flask.Flask(__name__)
app.debug = True
app.secret_key = 'iaeuwefLRN7DPU5vXAjr4gdGCdCvPY8BdjyFNHTzE8PfADcC'

gmail_user = 'xyz@gmail.com'
gmail_pwd = 'xxxxxx'

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
   text = flask.request.form['message']

   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = gmail_user
   msg['Subject'] = 'PGP Credibility'

   msg.attach(MIMEText(text))

   smtp = smtplib.SMTP('smtp.gmail.com', 587)
   smtp.ehlo()
   smtp.starttls()
   smtp.ehlo()
   smtp.login(gmail_user, gmail_pwd)
   smtp.sendmail(gmail_user, gmail_user, msg.as_string())
   smtp.quit()
   smtp.close()
   return 'Message has been successfuly sent!'

if __name__ == '__main__':
    app.run()
