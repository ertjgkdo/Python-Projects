from datetime import datetime
from operations import *
from write import *
from read import *

welcome_message()
continueLoop = True
while continueLoop == True:
    options()
    try:
        user_input = int(input("Enter 1,2 or 3: "))
        if user_input==1:
            laptop_orders = []
            display_inventory()
            total = buy_process(laptop_orders)
            buy_more = True
            while buy_more == True:
                buy = input("Do you want to buy more laptops?Y/N: ")
                if (buy == "y"or buy =="Y"):
                    total = total + buy_process(laptop_orders)
                else:
                    buy_more= False
            name, phone = final_message()
            company_name = "Shristi's Laptop Rental"
            vat_amt = 13/100
            gross_amt = total * (vat_amt) + total
            date_time = datetime.now()
            buy_bill(name, phone,company_name, date_time, laptop_orders, total, gross_amt)
            buy_invoice(name, phone,company_name, date_time, laptop_orders, total, gross_amt)
        elif user_input==2:
            sold_laptops =[]
            display_inventory()
            total = sell_process(sold_laptops)
            sell_more = True
            while sell_more == True:
                sell = input("Do you want to sell more laptops?Y/N: ")
                if (sell =="Y"or sell =="y"):
                    total = total + sell_process(sold_laptops)
                else:
                    sell_more = False
            name, phone = final_message()
            shipping_cost = 1500
            final_total, shipping_choice = shipping(total,shipping_cost)
            date_time = datetime.now()
            sell_bill(name, phone, date_time, sold_laptops, shipping_cost,shipping_choice,final_total)
            sell_invoice(name, phone, date_time, sold_laptops, shipping_cost,shipping_choice,final_total)
        elif user_input==3:
            continueLoop= False
        else:
            print("Please enter a correct option")
    except:
        print("Please input correct values")