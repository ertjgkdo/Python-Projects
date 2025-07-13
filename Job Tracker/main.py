from operations import *
from application import *
from tracker import *

continueLoop = True
job_tracker = Tracker()
while continueLoop == True:
    menu()
    user_choice = int(input("Enter choice:"))
    if user_choice == 1:
        company = input("Company: ")
        role = input("Role: ")
        status = input("Status (applied/interview/offer/rejected): ") or "applied"
        date = datetime.datetime.today().strftime("%Y-%m-%d") 
        application = Application(company,date, role, status)
        response = job_tracker.add(application)
        if response==1:
            add_success()
    elif user_choice==2:
        view()
        job_tracker.view_applications()
    elif user_choice==3:
        view()
        job_tracker.view_applications()
        index = int(input("Enter application number to update: "))-1
        new_status = input("Enter new status: ")
        job_tracker.update_status(index, new_status)
    elif user_choice==4:
        view()
        job_tracker.view_applications()
        index = int(input("Enter the application number to delete: "))-1
        job_tracker.delete_application(index)
    elif user_choice==5:
        job_tracker.summary()
    elif user_choice==6:
        continueLoop=False
    else:
        print("Please enter a correct option")

