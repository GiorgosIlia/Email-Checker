
import imapclient
import email
from email.header import decode_header

# IMAP server details (e.g., for Gmail)
server = "imap.gmail.com"
username = "yourgmail@gmail.com"
password = "yourPassWoords"
# Connect to the IMAP server
with imapclient.IMAPClient(server) as client:
    client.login(username, password)
    client.select_folder("INBOX")

    # Search for new, unread emails
    email_ids = client.search(["UNSEEN"])

    # Define the filter phrases
    filter_phrases = ["we will not", "unfortunately"]

    # Helper function to check if an email contains filter phrases
    def email_contains_filter_phrases(email_text):
        for phrase in filter_phrases:
            if phrase.lower() in email_text.lower():
                return True
        return False

    # Process and filter matching emails
    for email_id in email_ids:
        msg_data = client.fetch([email_id], ["RFC822"])
        msg_bytes = msg_data[email_id][b"RFC822"]
        msg = email.message_from_bytes(msg_bytes)
        subject, encoding = decode_header(msg["Subject"])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")

        # Get the email body
        email_body = msg.get_payload()
        email_text = email_body
        if isinstance(email_body, list):
            email_text = "".join([str(part.get_payload(decode=True), 'utf-8') for part in email_body if part.get_content_type() == 'text/plain'])

        if email_contains_filter_phrases(email_text):
            print(f"Filtered Email(Unfortunate news) - Subject: {subject}")
            # You can take further actions here, such as marking the email as read or moving it to a different folder.
        else:
            print(f"Unfiltered Email(You might want to check your unread emails! ) - Subject: {subject}")
