import BikeRentalSystem

class CompanyBank:
    Bankname = "Company National Bank"
    
    @classmethod
    def widthdraw(cls, amount, maccountnumber, mname, mphonenumber):
        BikeRentalSystem.BikeRentalSystem.companybalance = BikeRentalSystem.BikeRentalSystem.companybalance - amount
    
    @classmethod
    def deposit(cls, amount):
        BikeRentalSystem.BikeRentalSystem.companybalance = BikeRentalSystem.BikeRentalSystem.companybalance + amount
        print("Company balance", BikeRentalSystem.BikeRentalSystem.companybalance)