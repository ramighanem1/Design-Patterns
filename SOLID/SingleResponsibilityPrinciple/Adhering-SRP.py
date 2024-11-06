class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def change_email(self, new_email):
        self.email = new_email


class EmailNotifier:
    def __init__(self, user):
        self.user = user

    def notify(self, message):
        # Simulate sending an email
        print(f"Sending email to {self.user.email}: {message}")


# Usage
user = User("john_doe", "john@example.com")
notifier = EmailNotifier(user)

user.change_email("john.doe@example.com")
notifier.notify("Your email address has been changed.")
