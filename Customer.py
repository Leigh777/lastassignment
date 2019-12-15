
from numpy.distutils.fcompiler import none


class Customer:
    def __init__(self, cust_ID = None, fname = "", lname = "", company = "", street = "", city = "", state = "", zipcode = "", cust_name = "", cust_fulladdress = ""):
        self.__cust_ID = cust_ID
        self.__fname = fname
        self.__lname = lname
        self.__company = company
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zipcode = zipcode
        if cust_name is "":
            self.cust_name = fname + " " + lname
        if cust_fulladdress is "":
            if company is "":
                return street + "\n" + city + ", " + state + " " \
                       + zipcode
            else:
                return company + "\n" + street + "\n" + city + ", " + state + " " \
                       + zipcode





    @property
    def getcustomerid(self):
        return self.__cust_ID

    @property
    def getfname(self):
        return self.__fname

    @property
    def getlname(self):
        return self.__lname

    @property
    def getcompany(self):
        return self.__company

    @property
    def getstreet(self):
        return self.__street

    @property
    def getcity(self):
        return self.__city

    @property
    def getstate(self):
        return self.__state

    @property
    def getzipcode(self):
        return self.__zipcode

    @property
    def get_cust_name(self):
        if self.cust_name is "":
            self.cust_name = self.getfname + " " + self.getlname
        return self.cust_name

    @property
    def getcust_fulladdress(self):
        return self.cust_fulladdress

    @property
    def __get__(self):
        if self.cust_name is None:
            return self.getfname + " " + self.getlname

  #  def getcust_name(self, __fname, __lastname):
  #      cust_name = str(self.__fname) + " " + str(self.__lname)
  #      return cust_name


    def getcust_fulladdress(self, __street, __city, __state, __zipcode, __company):
        if __company is none:
            return str(self.__street) + "\n" + str(self.__city) + ", " + self.__state + " " \
                   + str(self.__zipcode)
        else:
            return str(self.__company) + "\n" + str(self.__street) + "\n" + str(self.__city) + ", " \
                   + self.__state + " " + str(self.__zipcode)

 #   @customerObject.setter
 #   def __str__(self, cust_name, cust_fulladdress):
  #      return str(self.cust_name) + "\n" + str(self.cust_fulladdress)

