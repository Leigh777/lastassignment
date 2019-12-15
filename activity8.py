#!/usr/bin/env python3
from Customer import *
import csv


def main():
    while True:
        try:
            read_csv_file()
            break
        except FileNotFoundError:
            print("Could not find file")
        except OSError:
            print("Error reading file")
            break


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
                CustomerItem.cust_name = str(CustomerItem.getfname) + " " + str(CustomerItem.getlname)
                #CustomerItem.cust_name = CustomerItem.__get__cust_name

                #       CustomerItem.cust_fulladdress = CustomerItem.getcust_fulladdress
                print(CustomerItem.getcustomerid, CustomerItem.getfname, CustomerItem.getlname, CustomerItem.getcompany,
                      CustomerItem.getstreet,
                      CustomerItem.getcity, CustomerItem.getstate, CustomerItem.getzipcode, CustomerItem.cust_name)
                customerlist.append(CustomerItem)

    return customerlist


if __name__ == "__main__":
    main()
