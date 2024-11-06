from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def attend_meeting(self):
        pass

    @abstractmethod
    def submit_timesheet(self):
        pass

class FullTimeEmployee(Employee):
    def work(self):
        return "Working full-time"

    def attend_meeting(self):
        return "Attending meeting"

    def submit_timesheet(self):
        return "Submitting timesheet"

class Intern(Employee):  # Interns may not need to submit timesheets or attend meetings
    def work(self):
        return "Working as an intern"

    def attend_meeting(self):
        raise NotImplementedError("Interns don't attend meetings")

    def submit_timesheet(self):
        raise NotImplementedError("Interns don't submit timesheets")

# Usage
full_time_employee = FullTimeEmployee()
intern = Intern()

print(full_time_employee.work())
print(intern.attend_meeting())  # Raises NotImplementedError
