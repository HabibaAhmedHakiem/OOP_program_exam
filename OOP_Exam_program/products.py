class Product:
    def __init__(self, id, name, description, retailPrice):
        self.id = id
        self.name = name
        self.description = description
        self.retailPrice = retailPrice

    def getDescription(self):
        return self.description

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getRetailPrice(self):
        return float(self.retailPrice)  # Convert to float

class Taxable:
    def __init__(self):
        pass

    def getTax(self):
        return 0.0

class Hardware(Product, Taxable):
    def __init__(self, id, name, description, retailPrice, warrantyPeriod):
        super().__init__(id, name, description, retailPrice)
        self.warrantyPeriod = warrantyPeriod

    def getWarrantyPeriod(self):
        return self.warrantyPeriod

class Software(Product):
    def __init__(self, id, name, description, retailPrice, license):
        super().__init__(id, name, description, retailPrice)
        self.license = license

    def getLicense(self):
        return self.license

    def getTax(self):
        # Add your logic to calculate tax for software
        return 0.05  # For example, 5% tax for software

    def getRetailPrice(self):
        try:
            return float(self.retailPrice)
        except ValueError:
            return 0.0


class Manual(Product):
    def __init__(self, id, name, description, retailPrice, publisher):
        super().__init__(id, name, description, retailPrice)
        self.publisher = publisher

    def getPublisher(self):
        return self.publisher


