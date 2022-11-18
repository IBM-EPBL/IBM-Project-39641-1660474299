import configparser
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


API = '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'
from_email = 'pragadeesh4701@gmail.com'
to_emails = 'harshaparthiban56789@gmail.com'
subject = "Hello"
html_content = "Happy to Learn.."

# def sendMailUsingSendGrid(API,from_email,to_emails,subject,html_content):
#     if API!=None and from_email!=None and len(to_emails)>0:
message = Mail(from_email,to_emails,subject,html_content)
try:
    sg = SendGridAPIClient(API)
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)



# sendMailUsingSendGrid(API,from_email,to_emails,subject,html_content)