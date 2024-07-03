import smtplib, ssl

receiver_email = "elizabethlorelei1229@gmail.com"
email = "grantbot08@gmail.com"

subject = "Grants List"
message = "Current list of grants: "

text = f"Subject: {subject}\n\n{message}"

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(email, "ialq guyh gbfg gztb")

server.sendmail(email, receiver_email, text)


