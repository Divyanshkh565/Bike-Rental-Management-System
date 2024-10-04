import CompanyBank
import Customer

class CustomerBank:
    Bankname = "Customer National Bank"
    
    @classmethod
    def widthdraw(cls, amount, maccountnumber, mname, mphonenumber):
        
        if mphonenumber == Customer.Customer.phonenumber and mname == Customer.Customer.name and maccountnumber == Customer.Customer.accountnumber:
            Customer.Customer.Balance = Customer.Customer.Balance - amount
            print("Customer balance", Customer.Customer.Balance)
            CompanyBank.CompanyBank.deposit(amount)
            
    @classmethod
    def deposit(cls, amount):
        Customer.Customer.Balance = Customer.Customer.Balance + amount