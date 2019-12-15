# Meg Harris Date Created: 11/26/19

import csv
from Customer import Customer

FILENAME = "customers.csv"


def get_customers():
    customers = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        # convert row to Customer object
        for row in reader:
            customer = Customer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            customers.append(customer)
    return customers


def show_customers(customers):
    print()
    print("ALL CUSTOMERS")
    print("-" * 20)
    print()

    for i in range(len(customers)):
        customer = customers[i]
        print(customer.cust_ID() + " : " + customer.cust_name())
    print()


def find_customer(cust_id, customers):
    for i in customers:
        if i.cust_ID() == cust_id:
            return i.cust_ID()
        else:
            return None
    return None
    print()


def main():
    customers = get_customers()
    show_customers(customers)

    choice = "y"
    while choice.lower()=="y":
        try:
            print()
            cust_id = int(input("Enter Customer ID: "))
            customer = find_customer(cust_id, customers)
            if customer == None:
                print("Customer " + str(cust_id) + " does not exist.")
                print()
                choice = input("Continue (y/n)?: ")
            else:
                print(customer)
                choice = input("Continue (y/n)?: ")
        except Exception as e:
            print(type(e), e)
    print("Bye!")


main()
