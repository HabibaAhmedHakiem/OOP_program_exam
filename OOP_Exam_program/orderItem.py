class OrderItem:
    def __init__(self, lineNbr, product, quantity):
        self.lineNbr = lineNbr
        self.product = product
        self.quantity = quantity

    def getItemTotal(self):
        return float(self.product.getRetailPrice()) * self.quantity

    def getLineNbr(self):
        return self.lineNbr

    def getProduct(self):
        return self.product

    def getQuantity(self):
        return self.quantity

    def getTax(self):
        return self.product.getTax()

    def getUnitPrice(self):
        return self.product.getRetailPrice()
