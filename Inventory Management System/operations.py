from datetime import datetime
from read import *

def welcome_message():
    print("\n")
    print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t Welcome to Shristi's Laptop Rental")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\tAddress: Lalitpur, Nepal")
    print("\t\t\t\t\t\t\t Contact: 9810022114")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")

def options():
    print("\n")
    print("Type 1 to buy from manufacturer")
    print("Type 2 to sell to customer")
    print("Type 3 to exit")

def name_check():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            return name
        else:
            print("Invalid Input. Please enter strings only")
def number_check():
    try:
        phone = int(input("Enter your phone number: "))
    except:
        print("Invalid Input! Please enter numerical values only")
        phone = int(input("Enter your phone number: ")) 
    return phone

def final_message():
    print("\n")
    print("Thank You For Buying!!")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("We will need your name and number to print the bill")
    name = name_check()
    phone = number_check()
    return name, phone

def display_inventory():
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("S.N\tName\t\t Brand \t\t Price \t\t Quantity \t Processor \t Graphic Card")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    a = 1
    with open("laptop.txt","r") as file:
        for line in file:
            print(a, "\t" + line.replace(",","\t"))
            a += 1
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("\n")

def buy_process(laptop_orders):
     ID = int(input("Please enter the ID of the laptop you want to buy from the manufacturer: "))
     ID=valid_input(ID)
     quantity = int(input("Please enter the quantity of the laptop you want to buy:"))
     quantity =valid_no(ID,quantity)
     net_amt = after_buy(ID, quantity, laptop_orders)
     return net_amt
     
def valid_input(input_id):
    while input_id <=0 or input_id > len(laptop):
        print("Invalid Laptop ID!!! Please enter a valid Laptop ID")
        print("\n")
        input_id = int(input("Please enter the ID of the laptop you want to buy: "))
    return input_id

def valid_no(input_id,input_no):
    user_quantity = int(laptop[input_id][3])
    while input_no<=0 or input_no>(user_quantity):
        print("Dear User, the laptop is out of stock, please retry!")
        print("\n")
        input_no = int(input("Please enter the quantity of the laptop you want to buy: "))
    return input_no

def after_buy(input_id, input_no, laptop_orders):
    valid_ID, valid_num= valid_input(input_id), valid_no(input_id,input_no)
    laptop[valid_ID][3] = int(laptop[valid_ID][3]) + int(valid_num)
    with open ("laptop.txt","w") as file:
        for values in laptop.values():
            file.write(str(values[0]) + ","+ str(values[1]) + ","+ str(values[2]) + "," + str(values[3]) + "," + str(values[4]) + "," + str(values[5]))
            file.write("\n")
            
    product_name = laptop[valid_ID][0]
    ordered_quantity = valid_num
    brand_name = laptop[valid_ID][1]
    laptop_price = int(laptop[valid_ID][2].replace("$"," "))
    total_price = laptop_price * ordered_quantity
    laptop_orders.append([product_name, ordered_quantity, laptop_price, brand_name, total_price])
    return total_price
    
    

def buy_bill(name, phone, company_name, date_time, laptop_orders, total, gross_amt):
    print("\n")
    print("\t \t \t \t \t\t\tOrder Bill: ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t Address: Lalitpur, Nepal \n")
    print("\t\t\t\t\t\t Contact:9810000000\n")
    print("\t\t\t\t\t Bill to the company: " + str(company_name))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Name:"+ str(name))
    print("Contact Number: " + str(phone))
    print("Date and time of purchase: "+ str(date_time))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Laptop Details are: ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------") 
    print("Item Name \t\t Total Quantity \t\t Laptop Brand \t\t Unit Price \t\t Total Price")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in laptop_orders:
        print(i[0],"\t\t\t", i[1],"\t\t\t", i[3], "\t\t","$", i[2], "\t\t", "$",i[4] ,"\n")
        print("\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Net Amount is: "+ str(total))
    print("Gross Amount is:"+ str(gross_amt))
    print("**************************************************\t NOTE: 13% VAT is applied to this purchase \t*************************************************")
    

def sell_process(sold_laptops):
    ID = int(input("Please enter the ID of the laptop the customer wants to buy: "))
    ID=valid_input(ID)
    quantity = int(input("Please enter the quantity of the laptop you want to buy:"))
    quantity = valid_no(ID,quantity)
    net_amt = after_sell(ID,quantity,sold_laptops)
    return net_amt

def after_sell(input_id, input_no,sold_laptops):
    valid_id, valid_num = valid_input(input_id), valid_no(input_id, input_no)
    laptop[valid_id][3] = int(laptop[valid_id][3])-int(valid_num)
    with open("laptop.txt","w") as file:
        for values in laptop.values():
            file.write(str(values[0]) + "," + str(values[1]) +"," + str(values[2]) +","+ str(values[3])+","+ str(values[4])+","+ str(values[5]))
            file.write("\n")
    product_name = laptop[valid_id][0]
    ordered_quantity = valid_num
    brand_name = laptop[valid_id][1]
    laptop_price = int(laptop[valid_id][2].replace("$"," "))
    total_price = laptop_price * ordered_quantity
    sold_laptops.append([product_name, ordered_quantity, laptop_price, brand_name, total_price])
    return total_price

def shipping(total,shipping_cost):
    shipping = input("Dear user, Do you want your products to be shipped or not?(Y/N): ")
    if(shipping =="y" or shipping =="Y"):
        grand_total = total + shipping_cost
        return grand_total, True
    else:
        grand_total = total
        return grand_total, False

def sell_bill(name, phone, date_time, sold_laptops, shipping_cost,shipping_choice,final_total):
    print("\n")
    print("\t\t\t\t\t\t\t Shristi's Laptop Rental")
    print("\t\t\t\t\t\t\t Address: Lalitpur,Nepal")
    print("\t\t\t\t\t\t\t   Contact:9810000000")
    print("\t\t\t\t\t\t\t\t BILL: ")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Name of the customer:"+ str(name))
    print("Contact Number: "+ str(phone))
    print("Date and Time of purchase: "+ str(date_time))
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Purchase Details are: \n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Item Name \t\t Total Quantity \t\t Laptop Brand \t\t Unit Price \t\t Total Price")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    for i in sold_laptops:
        print(i[0], "\t\t\t", i[1], "\t\t\t", i[3],"\t\t","$", i[2], "\t\t\t","$",i[4])
        print("\n")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------------")
    if shipping_choice:
        print("Your shipping cost is: ", shipping_cost)
        print("Grand Total: $"+ str(final_total))
        print("*************************************************\t Note: Shipping cost is added to the grand total \t*****************************************")
    else:
        print("Grand Total: $" + str(final_total))
        print("**************************************************\t Thankyou for selling to the customer \t******************************************************")