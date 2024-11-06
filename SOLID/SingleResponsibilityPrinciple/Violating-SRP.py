class UserManager:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def change_email(self, new_email):
        # Update email address
        self.email = new_email
        # Notify user about the change
        self.notify_user("Your email address has been changed.")

    def notify_user(self, message):
        # Simulate sending an email
        print(f"Sending email to {self.email}: {message}")

# Usage
user = UserManager("john_doe", "john@example.com")
user.change_email("john.doe@example.com")
