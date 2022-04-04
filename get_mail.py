import datetime
import imaplib
import re
import email

def get_mail(email_account, password):
    mail = imaplib.IMAP4_SSL('imap.mail.ru')
    mail.login(email_account, password)
    mail.list()
    mail.select('inbox')
    result, data = mail.uid('search', None, "UNSEEN")  # (ALL/UNSEEN)
    i = len(data[0].split())
    for x in range(i):
        latest_email_uid = data[0].split()[x]
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        # result, email_data = conn.store(num,'-FLAGS','\\Seen')
        # this might work to set flag to seen, if it doesn't already
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)

        # Header Details
        date_tuple = email.utils.parsedate_tz(email_message['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
            local_message_date = "%s" %(str(local_date.strftime("%a, %d %b %Y %H:%M:%S")))
        email_from = str(email.header.make_header(email.header.decode_header(email_message['From'])))
        email_to = str(email.header.make_header(email.header.decode_header(email_message['To'])))
        subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))

        # Body details
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                output_file = open("email.txt", 'w', encoding="utf-8")
                text = f"From: {email_from}\nTo: {email_to}\nDate: {local_message_date}\nSubject: {subject}\n\nBody: \n\n{body.decode('ISO-8859-1')}"
                output_file.write(text)
                for var in range(5):
                    try:
                        f = re.findall('https://privetsecret.com/confirm[\S]+', text)
                        f = f[0]
                        f = f.replace(")", "")
                        output_file.close()
                        return f
                    except:
                        continue
            else:
                continue
