import smtplib
import config
from utils.get_templates import get_html_template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_alerting_email():
    message_template = get_html_template()
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(config.smtp_email, config.smtp_password)
    for email in config.recipient_list:
        msg = MIMEMultipart()       # create a message
        # add in the actual person name to the message template
        message = message_template.substitute()
        # setup the parameters of the message
        msg['From']=config.smtp_email
        msg['To']=email
        msg['Subject']="This is TEST"
        # add in the message body
        msg.attach(MIMEText(message, 'html'))
        # send the message via the server set up earlier.
        s.send_message(msg)
        del msg
    # Terminate the SMTP session and close the connection
    s.quit()
    return('email sent :)')