from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Attendable(ABC):
    @abstractmethod
    def attend_meeting(self):
        pass

class TimesheetSubmittable(ABC):
    @abstractmethod
    def submit_timesheet(self):
        pass

class FullTimeEmployee(Workable, Attendable, TimesheetSubmittable):
    def work(self):
        return "Working full-time"

    def attend_meeting(self):
        return "Attending meeting"

    def submit_timesheet(self):
        return "Submitting timesheet"

class Intern(Workable):  # Intern only implements what it needs
    def work(self):
        return "Working as an intern"

# Usage
full_time_employee = FullTimeEmployee()
intern = Intern()

print(full_time_employee.work())
print(intern.work())  # No longer forced to implement unnecessary methods
