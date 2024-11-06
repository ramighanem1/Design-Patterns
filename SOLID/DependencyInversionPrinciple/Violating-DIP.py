class Database:
    def connect(self):
        return "Connecting to the database"

class DataHandler:
    def __init__(self):
        self.db = Database()  # Direct dependency on a low-level module

    def handle_data(self):
        return self.db.connect()  # High-level module depends on low-level module

# Usage
handler = DataHandler()
print(handler.handle_data())