import smtplib
from twilio.rest import Client

MY_EMAIL = "190020116012ait@gmail.com"
MY_PASSWORD = "Salvatore@02"


class NotificationManager:
    def __init__(self):
        self.TWILIO_ACCOUNT_SID = "AC99b8cb62e18f6f42714f02ebf45cfaad"
        self.TWILIO_AUTH_TOKEN = "1565d97c6b91a9524d74935a3fa44bc1"
        self.client = Client(self.TWILIO_ACCOUNT_SID, self.TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+19033293521",
            to="+919974595905",
        )
        print(message.sid)
        pass

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
