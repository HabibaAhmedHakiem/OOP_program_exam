from datetime import date
from OOP_Exam_program.orderItem import OrderItem

class Order:
    def __init__(self, id, customer):
        self.id = id
        self.customer = customer
        self.items = []

    def addOrderItem(self, product):
        item = OrderItem(len(self.items) + 1, product, 0)
        self.items.append(item)
        return item

    def add_product_to_cart(self, product):
        found = False
        for item in self.items:
            if item.getProduct().getId() == product.getId():
                item.quantity += 1
                found = True
                break
        if not found:
            item = self.addOrderItem(product)
            item.quantity += 1

    def getCustomer(self):
        return self.customer

    def getId(self):
        return self.id

    def getItems(self):
        return self.items

    def getOrderDate(self):
        return date.today().strftime("%Y-%m-%d")

    def getOrderTotal(self):
        total = 0
        for item in self.items:
            total += item.getItemTotal()
        return total

    def print_order_receipt(self):
        print("------------------ Order data -----------------")
        print(f"Order id = {self.getId()}")
        print(f"Customer name = {self.get}")
