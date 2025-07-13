import os
import json
import application
class Tracker:
    def __init__(self, filename = 'data.json'):
        self.filename = filename
        self.applications = self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return[]
        with open(self.filename, 'r') as data:
            return json.load(data)
    
    def save(self):
        with open(self.filename, "w") as data:
            json.dump(self.applications, data, indent=4)

    def add(self, application):
        self.applications.append(application.to_dict())
        self.save()
        return 1
        
    def view_applications(self):
        if not self.applications:
            print("No applications yet.")
            return
        for index, entry in enumerate(self.applications):
            print(f"{index+1}. {entry['company']} - {entry['role']} ({entry['status']}) on {entry['applied_date']}")

    def update_status(self, index, new_status):
        try:
            self.applications[index]['status'] = new_status
            self.save()
            print("Status updated.")
        except IndexError:
            print("Invalid index.")

    def delete_application(self, index):
        try:
            removed = self.applications.pop(index)
            self.save()
            print(f"Deleted application for {removed['company']} - {removed['role']}")
        except IndexError:
            print("Invalid index.")

    def summary(self):
        count = {}
        for app in self.applications:
            status = app['status']
            count[status] = count.get(status, 0) + 1
        print("Application Summary:")
        for status, total in count.items():
            print(f"{status.capitalize()}: {total}")