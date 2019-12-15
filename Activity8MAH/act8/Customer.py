# Meg Harris Date Created: 11/26/19

class Customer:
    #a constructor that initializes the attributes
    def __init__(self, cust_ID, fName, lName, company, street, city, state, zipcode):
        self.__cust_ID = cust_ID
        self.__fName = fName
        self.__lName = lName
        self.__company = company
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode

    def cust_name(self):
        return str(self.__fName + " " + self.__lName)

    def cust_fullAddress(self):
        if self.__company == "":
            fullAddress = str(self.__street + "\n" + self.__city + self.__state + self.__zipcode)
        else:
            fullAddress = str(self.__company + "\n" + self.__street + "\n" + self.__city + self.__state + self.__zipcode)
        return fullAddress

    def cust_ID(self):
        return self.__cust_ID

    def cust_company(self):
        return self.__company

    def __str__(self):
        value = self.cust_name() + self.cust_fullAddress()
        return value
