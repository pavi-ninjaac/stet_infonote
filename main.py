from fetch_mangodb import fetch_mangidb_data
import smtplib,ssl
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#convert the pdf to png formate this function convert the pdf file and save it as png and give you the image path
#here return image path will be inside the list so indexing is must while using that path
#document_dict,records_dict=fetch_mangidb_data.fetch_data()
#print(document_dict)
#print(records_dict)
#_________________comaprision code goes  here
#________________________________send mail
valid=True
if(valid==True):


    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python"



    sender_email = "stet.infonote@gmail.com"
    receiver_email = "stet.infonote@gmail.com"
    password = 'stet123infonote'

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    #___________________document insides
    msg_doc=""" ADMIT CARD
    STATE ELIGIBILITY 
    
    """

    filename = "do.pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, 'rb') as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload((attachment).read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Decomposition",
        "attachment", filename= filename,
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
else:
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "stet.infonote@gmail.com"  # Enter your address
    receiver_email = "stet.infonote@gmail.com"  # Enter receiver address
    password = 'stet123infonote'
    NAME="pavi"
    message = """\
    Subject: Hi there {%NAME}

    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)





