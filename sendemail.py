import sendgrid
from sendgrid.helpers import mail
try:
    # Python 3
    import urllib.request as urllib
except ImportError:
    # Python 2
    import urllib2 as urllib

SENDGRID_API_KEY = "YOUR_SENDGRID_API_KEY"
SENDGRID_SENDER_EMAIL = "from@email.com"
SENDGRID_SENDER_NAME = "From Name"
SENDGRID_RECIPIENT_EMAIL = "to@email.com"

sg = sendgrid.SendGridAPIClient(apikey = SENDGRID_API_KEY)

from_email = mail.Email(SENDGRID_SENDER_EMAIL, SENDGRID_SENDER_NAME)
to_email = mail.Email(SENDGRID_RECIPIENT_EMAIL)

subject = "Status for Today"

# For plain text content
content = mail.Content("text/plain", "Sensor is Offline")

# For HTML content
#content = mail.Content("text/html", "<html><body><h1>Station is Offline</h1></body></html>")

message = mail.Mail(from_email, subject, to_email, content)

try:
    response = sg.client.mail.send.post(request_body=message.get())
except urllib.HTTPError as e:
    print (e.read())
    exit()

# Print response from SendGrid service
print(response)
print(response.status_code)
print(response.body)
print(response.headers)