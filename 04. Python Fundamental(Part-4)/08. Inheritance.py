class Employee:
    start_time = "8am"
    end_time = "6pm"
    
class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject
    
    def change_time(self, new_start_time):
        self.start_time = new_start_time


class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role
    def role_change(self, new_role):
        self.role = new_role

staff1 = AdminStaff('Manager')
staff1.role_change('Senior Manager')
print(staff1.role, staff1.start_time, staff1.end_time)

# t1 = Teacher("Math")
# t1.change_time("10am")
# print(t1.subject, t1.start_time, t1.end_time)
        
        