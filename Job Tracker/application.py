import datetime
class Application:
    def __init__(self, company, date, role,status):
        self.company = company
        self.role = role
        self.status = status or 'applied'
        self.date = date or datetime.today()
        
    def to_dict(self):
        return {
            "company": self.company,
            "role": self.role,
            "status": self.status,
            "applied_date": self.date
        } 
        