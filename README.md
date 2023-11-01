# Email Filter with IMAPClient

This Python script allows you to connect to an email account using the IMAP protocol and filter emails based on specific phrases in the email content. In this example, we use the `imapclient` library to connect to a Gmail account, search for new, unread emails, and filter out emails containing the phrases "we will not" and "unfortunately."

## Prerequisites

- Python 3.x
- The `imapclient` library. You can install it using `pip`:
  ```
  pip install imapclient
  ```

## Usage

1. Clone or download this repository to your local machine.
2. Open the script and edit the following variables with your own information:

   - `server`: The IMAP server address (e.g., "imap.gmail.com" for Gmail).
   - `username`: Your email address (e.g., "yourgmail@gmail.com").
   - `password`: Your App-Specific Password (more details below).

3. Ensure that your email account has Two-Factor Authentication (2FA) enabled as per Google's new security policy in 2022.

4. Run the script:

   ```shell
   python email_filter.py
   ```

5. The script will connect to your email account, search for new, unread emails, and filter them based on the specified phrases. Filtered emails will be printed with a message indicating why they were filtered, and unfiltered emails will be printed to alert you to check your unread emails.

## App-Specific Password

Google recommends using App-Specific Passwords when accessing your Gmail account via third-party applications. To generate an App-Specific Password:

1. Go to your Google Account settings.
2. Click on "Security" in the left navigation panel.
3. Under "Signing in to Google," find the "App passwords" section.
4. Generate a new app password for your script.
5. Replace the `password` variable in the script with the generated App-Specific Password.

## Note

- Google's Two-Factor Authentication (2FA) should be enabled for your account. This script requires an App-Specific Password to access your Gmail account.

- It's essential to keep your App-Specific Password secure and not share it with others.

- The script provided is a basic example and can be further customized to suit your specific needs.

Feel free to modify and use this script to filter emails based on your own criteria and email providers.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Happy emailing!