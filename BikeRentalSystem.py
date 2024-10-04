import Customer
import CustomerBank

class BikeRentalSystem:
    companyname = "Bike Rental pvt. ltd."
    companynumber = 1234567890
    accountnumber = 111111111111
    companybalance = 0

    def __init__(self):
        while True:
            print("\n")
            print("*"*40)
            print(f"Welcome to {BikeRentalSystem.companyname}!")
            print("*"*40)
            print("\n")
            print("Press 1 to rent bike on hour basis(200 rupee per hour)")
            print("Press 2 to rent bike on day basis(500 rupee per day)")
            print("Press 3 to rent bike on week basis(1500 rupee per week)")
            print("Press 4 to quit")
            inp = int(input(">>"))
            if inp == 1:
                hours = int(input("For how many hours??\n>>"))
                BikeRentalSystem.payment(hours*200, Customer.Customer.name, Customer.Customer.accountnumber, Customer.Customer.phonenumber)
            elif inp == 2:
                days = int(input("For how many days??\n>>"))
                BikeRentalSystem.payment(days*500, Customer.Customer.name, Customer.Customer.accountnumber, Customer.Customer.phonenumber)
            elif inp == 3:
                weeks = int(input("For how many weeks??\n>>"))
                BikeRentalSystem.payment(weeks*1500, Customer.Customer.name, Customer.Customer.accountnumber, Customer.Customer.phonenumber)
            elif inp == 4:
                quit()
    @classmethod
    def payment(cls, amount, name, accountnumber, phonenumber):
        CustomerBank.CustomerBank.widthdraw(amount, accountnumber, name, phonenumber)

if __name__ == "__main__":
    comp = BikeRentalSystem()