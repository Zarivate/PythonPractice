# Google no longer supports less secure app access so this program is sadly moot
import smtplib

sender = "gmailhere"
receiver = "gmailhere"
password = "Password here"
subject = "Python email test"
body = "If you're reading this then it was a success!"

# Triple quotes means that can span multiple lines of text, useful for the header of the email below
message = f"""From: Dongus Dingle {sender}
To: A very person person {receiver}
Subject: {subject}\n
{body}
"""

# Server object, will use default mail submission port for second argument
server = smtplib.SMTP("smtp.gmail.com", 587)
# Start the transport layer security
server.starttls()

try:
    server.login(sender,password)
    print("I'm in...")
    server.sendmail(sender,receiver, message)
    print("Email has been sent!")

except smtplib.SMTPAuthenticationError:
    print("Something went wrong, couldn't sign in")