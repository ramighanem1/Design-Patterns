from abc import ABC, abstractmethod

# Abstraction that both high-level and low-level modules depend on
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self):
        pass

# Low-level module
class MySQLDatabase(DatabaseConnection):
    def connect(self):
        return "Connecting to MySQL database"

# Low-level module
class PostgreSQLDatabase(DatabaseConnection):
    def connect(self):
        return "Connecting to PostgreSQL database"

# High-level module now depends on abstraction
class DataHandler:
    def __init__(self, db: DatabaseConnection):  # Dependency Injection
        self.db = db

    def handle_data(self):
        return self.db.connect()  # High-level module uses the abstraction

# Usage
mysql_db = MySQLDatabase()
postgres_db = PostgreSQLDatabase()

handler = DataHandler(mysql_db)  # Inject MySQLDatabase dependency
print(handler.handle_data())  # Output: "Connecting to MySQL database"

handler = DataHandler(postgres_db)  # Inject PostgreSQLDatabase dependency
print(handler.handle_data())  # Output: "Connecting to PostgreSQL database"