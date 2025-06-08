import smtplib
from email.mime.text import MIMEText
from utils.config import EMAIL_USER, EMAIL_PASSWORD, RECEIVER_EMAIL, SMTP_SERVER, SMTP_PORT

def send_email_alert(message):
    # Create the email content
    msg = MIMEText(message)
    msg['Subject'] = 'Thief Detected Alert'
    msg['From'] = EMAIL_USER
    msg['To'] = RECEIVER_EMAIL

    # Connect to the email server and send the alert
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, RECEIVER_EMAIL, msg.as_string())

    print("Alert email sent successfully.")
