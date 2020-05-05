import config
from selenium import webdriver
from selenium.webdriver.common.by import By
import urllib.request
driver = webdriver.Chrome()
from datetime import datetime


driver.get("http://books.toscrape.com/catalogue/category/books_1/index.html")
driver.save_screenshot('screenie.png')

# elems = driver.find_elements_by_css_selector(".browse-story-item completed [href]")
# links = [elem.get_attribute('href') for elem in elems]

# print(elems)

a_elements = []
content_blocks = driver.find_elements_by_class_name("product_pod")

for block in content_blocks:
    elements = block.find_elements_by_tag_name("h3 a")
    for el in elements:
        a_elements.append(el.get_attribute("innerHTML"))

imagesArray = []    
images = driver.find_elements_by_tag_name('img')
for image in images:
    src = image.get_attribute('src')
    print(src)
    imagesArray.append(src)

driver.close()

import smtplib

# import the corresponding modules
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtp_server = "smtp.gmail.com"
login = "devngecu@gmail.com" # paste your login generated by Mailtrap
password = "Facebookme1" # paste your password generated by Mailtrap

subject = "An example of boarding pass"
sender_email = "devngecu@gmail.com"
receiver_email = "ngecu16@gmail.com"

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

# Add body to email
body = "This is an example of how you can send a boarding pass in attachment with Python"
message.attach(MIMEText(body, "plain"))

filename = "screenie.png"
# Open PDF file in binary mode

# We assume that the file is in the directory where you run your Python script from
with open(filename, "rb") as attachment:
    # The content type "application/octet-stream" means that a MIME attachment is a binary file
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode to base64
encoders.encode_base64(part)

# Add header 
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to your message and convert it to string
message.attach(part)
text = message.as_string()

# send your email
with smtplib.SMTP("smtp.gmail.com",587) as server:
    print(sender_email)
    server.ehlo()
    server.starttls()
    server.login('devngecu@gmail.com', password)
    server.sendmail(
        sender_email, receiver_email, text
    )
    server.quit()
print('Sent') 

