from datetime import datetime
import os

clock = datetime.now()
d1 = clock.strftime("%B %d, %Y @ %H:%M:%S")
path = os.getlogin()
print('programmer: ', path)
print("Lab 19.4", end=' ')
print(d1)
print(" ")
class Person:
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone_number(self):
        return self.__phone_number

class Customer(Person):
    def __init__(self, name, address, phone_number, customer_number, mailing_list):
        Person.__init__(self, name, address, phone_number)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list

def main():
    name = input("Enter your name: ")
    customer = input("Enter the customers name: ")
    address = input("Enter the customer's address: ")
    phone = input("Enter the customer's phone_number: ")
    number = int(input("Enter the customers number: "))
    wish = input("Does the customer wish to be on the mailing list?(Yes/No): ")
    if wish == "yes":
        desic = True
    else:
        desic = False

    print(f"{name}, here is the customer, {customer}'s information:")
    print()
    customer = Customer(customer, address, phone, number, desic)
    print("Name:", customer.get_name())
    print("Address:", customer.get_address())
    print("Phone Number:", customer.get_phone_number())
    print("Customer Number:", customer.get_customer_number())
    print("Mailing List:", customer.get_mailing_list())

main()
