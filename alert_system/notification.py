def send_sms_alert(phone_number, message):
    # Integrate with a SMS gateway service
    print(f"SMS sent to {phone_number}: {message}")

if __name__ == "__main__":
    send_sms_alert('+1234567890', 'A thief has been detected!')
