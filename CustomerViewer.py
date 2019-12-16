#Leigh Kuhry 12/15/2019 CIST4900
#!/usr/bin/env python3
from Customer import *
from numpy.distutils.fcompiler import none
import csv


def main():
    while True:
        try:
            customerlist = read_csv_file()
            break
        except FileNotFoundError:
            print("Could not find file")
        except OSError:
            print("Error reading file")
            break
    displaycustidname(customerlist)
    choice = "y"
    while True:
        if choice.lower() == "y":
            customeridvalue = str(input("Enter Customer ID: "))
            chosenCustomer = getcustomerbyid(customeridvalue, customerlist)
            choice = (str(input("Would you like to contine?")))
        elif choice.lower() == 'n':
            break
        else:
            print("Answer needs to be a 'y' or 'n'. Try again.")
            choice = (str(input("Would you like to contine?")))


def getcustomerbyid(customeridvalue, customerlist):
    for i in customerlist:
        if i.cust_ID == customeridvalue:
            # figure out how to print entire object
            print("\n")
            print(i())
            print("\n")
            return i.cust_ID
        else:
            continue
    print ("Customer ", customeridvalue, "does not exist \n")
    return None

def displaycustidname(customerlist):
    print("CUSTOMER VIEWER" + "\n \n")
    print(" All Customers ")
    print("----------------")

    for i in customerlist:
        print (i.cust_ID, i.cust_name)
    print("\n \n")

def read_csv_file():
    customerlist = []
    with open("customers.csv", 'r') as f:
        reader = csv.reader(f)
        firstline = True
        for row in reader:
            if firstline:  # skip first line
                firstline = False
                continue
            else:
                CustomerItem = (Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
                cust_name = CustomerItem.cust_name
                cust_fulladdress = CustomerItem.cust_fulladdress
                customerlist.append(CustomerItem)

    return customerlist


if __name__ == "__main__":
    main()
