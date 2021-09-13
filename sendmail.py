from celery import Celery
import smtplib

app = Celery("send_email_service", broker="amqp://guest:guest@localhost:5672//")

app.conf.task_default_exchange = "send_email_service"
app.conf.task_default_routing_key = "send_email_service"
app.conf.task_default_queue = "send_email_service"


@app.task()
def sendMail(sender, receiver, password, message, operator, num1, num2):
    #print("Select Choice :")
    #print("1 for Addition")
    #print("2 for Subtraction")
    #print("3 for Multiplication")
    #print("4 for Division")
    #print("5 for Power")
    #choice = input("Enter Your Choice : ")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    choice = operator
    server.starttls()
    server.login(sender, password)
    if choice == "1":
        message = "Addition of " + str(num1) + " and " + str(num2) + " is " + str(num1 + num2) + ". \n" + message
        server.sendmail(sender, receiver, message)
        return "All the test cases passed"
    elif choice == "2":
        message = "Subtraction of " + str(num1) + " and " + str(num2) + " is " + str(num1 - num2) + ". \n" + message
        server.sendmail(sender, receiver, message)
        return "All the test cases passed"
    elif choice == "3":
        message = "Multiplication of " + str(num1) + " and " + str(num2) + " is " + str(num1 * num2) + ". \n" + message
        server.sendmail(sender, receiver, message)
        return "All the test cases passed"
    elif choice == "4":
        message = "Division of " + str(num1) + " and " + str(num2) + " is " + str(num1 / num2) + ". \n" + message
        server.sendmail(sender, receiver, message)
        return "All the test cases passed"

    elif choice == "**":
        message = "Power of " + str(num1) + " to " + str(num2) + " is " + str(num1 ** num2) + ". \n" + message
        server.sendmail(sender, receiver, message)
        return "All the test cases passed"
    else:
        return "PLEASE CHOOSE CORRECT CHOICE"