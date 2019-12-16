



class Customer:
    def __init__(self, cust_ID, fname, lname, company, street, city, state, zipcode):
        self.__cust_ID = cust_ID
        self.__fname = fname
        self.__lname = lname
        self.__company = company
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode


    @property
    def cust_ID(self):
        return self.__cust_ID

    @property
    def fname(self):
        return self.__fname

    @property
    def lname(self):
        return self.__lname

    @property
    def company(self):
        return self.__company

    @property
    def street(self):
        return self.__street

    @property
    def city(self):
        return self.__city

    @property
    def state(self):
        return self.__state

    @property
    def zipcode(self):
        return self.__zipcode

    @property
    def cust_name(self):
        return str(self.fname) + " " + str(self.lname)

    @property
    def cust_fulladdress(self):
        if self.__company is "":
            return str(self.__street) + "\n" + str(self.__city) + ", " + str(self.__state) + " " \
                   + str(self.__zipcode)
        else:
            return str(self.__company) +"\n" + str(self.__street) + "\n" + str(self.__city) + ", " + str(self.__state) + " " + str(self.__zipcode)

    @property
    def customer(self):
        return str(self.cust_name) + "\n" + str(self.cust_fulladdress)

    def __str__(self):
        return str(self.cust_name) + "\n" + str(self.cust_fulladdress)

    def __call__(self):
        return str(self.cust_name) + "\n" + str(self.cust_fulladdress)

