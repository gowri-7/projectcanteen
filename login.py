import csv
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def register(username, password):
    with open('users.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password])
        print("account succesfully created")
def login(username, password):
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username and row[1] == password:
                 return True
                 print("login successful")
                 break
        else:
            return False
            print("login failed")

def man():
    while True:
        choice = input("Choose an option:\n1. Sign up\n2. Login\n3. Quit\n")
        if choice == '1':
            username = input("Enter admission number: ")
            email= input("Enter email: ")
            otp=input("enter otp send in mail")
def send_email(email, otp):
    sender_email = "your_email@gmail.com"  # Your email
    sender_password = "your_password"      # Your email password

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = email
    message['Subject'] = "OTP Verification"

    body = f"Your OTP is: {otp}"
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = message.as_string()
    server.sendmail(sender_email, email, text)
    server.quit()

def generate_otp():
    return str(random.randint(100000, 999999))

def main():
    email = input("Enter your email: ")
    otp = generate_otp()
    send_email(email, otp)

    user_otp = input("Enter the OTP sent to your email: ")

    if user_otp == otp:
        new_password = input("Enter your new password: ")
        print("Password set successfully!")
    else:
        print("Invalid OTP. Please try again.")

            register(username, password)
            print("Account created successfully!")
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            if login(username, password):
                print("Login successful!")
            else:
                print("Invalid username or password.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
man() 