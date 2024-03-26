class Customer:
    def __init__(self, customerId, firstName, lastName, email, phone, address):
        self.__customerId = customerId
        self.__firstName = firstName
        self.__lastName = lastName
        self.__email = email
        self.__phone = phone
        self.__address = address

    def getCustomerId(self):
        return self.__customerId

    def setCustomerId(self, customerId):
        self.__customerId = customerId

    def getFirstName(self):
        return self.__firstName

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def getLastName(self):
        return self.__lastName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def getEmail(self):
        return self.__email

    def setEmail(self, email):
        self.__email = email

    def getPhone(self):
        return self.__phone

    def setPhone(self, phone):
        self.__phone = phone

    def getAddress(self):
        return self.__address

    def setAddress(self, address):
        self.__address = address

    def displayCustomerInfo(self):
        print("Customer ID:", self.__customerId)
        print("First Name:", self.__firstName)
        print("Last Name:", self.__lastName)
        print("Email Address:", self.__email)
        print("Phone Number:", self.__phone)
        print("Address:", self.__address)
