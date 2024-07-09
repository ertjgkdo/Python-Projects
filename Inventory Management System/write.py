from read import *
from operations import *

def buy_invoice(name, phone,company_name, date_time,laptop_orders, total, gross_amt):
    with open(str(name) + str(phone) + ".txt","w")as file:
        file.write("\n")
        file.write("\t \t \t \t \t\t\tOrder Bill: \n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\t\t\t\t\t\t Address: Lalitpur, Nepal \n")
        file.write("\t\t\t\t\t\t Contact:9810000000\n")
        file.write("\t\t\t\t\t Bill to the company: " + str(company_name))
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("Name:"+ str(name) +"\n")
        file.write("Contact Number: " + str(phone)+"\n")
        file.write("Date and time of purchase: "+ str(date_time)+"\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("Laptop Details are: \n")
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("Item Name \t\t Total Quantity \t\t Laptop Brand \t\t Unit Price \t\t Total Price")
        file.write("\n")
        for i in laptop_orders:
            file.write(str(i[0]) + "\t\t\t"+ str(i[1]) + "\t\t"+ str(i[3]) + "\t\t\t"+ "$"+ str(i[2]) + "\t\t\t"+"$"+str(i[4]))
            file.write("\n")
        file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        file.write("Net Amount is: "+ str(total) + "\n")
        file.write("Gross Amount is: " + str(gross_amt) + "\n")
        file.write("**************************************************\t NOTE: 13% VAT is applied in this product \t*************************************************")
            

def sell_invoice(name, phone, date_time, sold_laptops, shipping_cost,shipping_choice,final_total):
    with open(str(name) + str(phone) + ".txt", "w")as file:
        file.write("\n")
        file.write("\t\t\t\t\t\t\t Shristi's Laptop Rental \n")
        file.write("\t\t\t\t\t\t\t Address: Lalitpur,Nepal \n")
        file.write("\t\t\t\t\t\t\t   Contact: 9810000000 \n")
        file.write("\t\t\t\t\t\t\t\t BILL: ")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("Name of the customer:"+ str(name)+"\n")
        file.write("Contact Number: "+ str(phone)+"\n")
        file.write("Date and Time of purchase: "+ str(date_time)+"\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("Purchase Details are: \n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        file.write("Item Name \t\t Total Quantity \t\t Laptop Brand \t\t Unit Price \t\t Total Price")
        file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        for i in sold_laptops:
            file.write(str(i[0]) + "\t\t\t"+ str(i[1]) + "\t\t\t"+ str(i[3]) + "\t\t\t"+ "$"+ str(i[2]) + "\t\t\t" + "$"+str(i[4]))
            file.write("\n")
        file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------")
        file.write("\n")
        if shipping_choice:
            file.write("Your shipping cost is: " + str(shipping_cost)+"\n")
            file.write("Grand Total: $"+ str(final_total) +"\n")
            file.write("*************************************************\t Note: Shipping cost is added to the grand total \t*****************************************")
        else:
            file.write("Grand Total: $" + str(final_total) +"\n")
            file.write("**************************************************\t Thankyou for selling to the customer \t******************************************************")
        