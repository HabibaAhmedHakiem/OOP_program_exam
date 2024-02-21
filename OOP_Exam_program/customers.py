class Customer:
    def __init__(self, id, name, phone, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address

    def getAddress(self):
        return self.address

    def getid(self):
        return self.id

    def getName(self):
        return self.name

    def getPhone(self):
        return self.phone

    def setAddress(self, new_address):
        self.address = new_address

    def setid(self, new_id):
        self.id = new_id


class Company(Customer):
    def __init__(self, id, name, phone, address, contact, discount):
        super().__init__(id, name, phone, address)
        self.contact = contact
        self.discount = discount

    def getContact(self):
        return self.contact

    def getDiscount(self):
        return self.discount

    def setContact(self, new_contact):
        self.contact = new_contact


class Individual(Customer):
    def __init__(self, id, name, phone, address, licNumber):
        super().__init__(id, name, phone, address)
        self.licNumber = licNumber

    def getLicNumber(self):
        return self.licNumber

    def setLicNumber(self, new_lic_number):
        self.licNumber = new_lic_number
