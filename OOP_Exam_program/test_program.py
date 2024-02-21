from datetime import date
from OOP_Exam_program.customers import Company
from OOP_Exam_program.orders import Order
from OOP_Exam_program.products import Hardware, Software
import unittest
from OOP_Exam_program.customers import Company, Individual
from OOP_Exam_program.products import Hardware, Software, Manual

keyboard = Hardware(1, "keyboard", "Accessory", 100, 3)
office2022 = Software(2, "office 2022", "Ms Office", 200, "554-65-211")

raya = Company(1002, "Raya Co.", "01012312312", "Cairo", "Ahmed Mostafa", 0.0)

my_order = Order(1002, raya)

my_order.add_product_to_cart(office2022)
my_order.add_product_to_cart(keyboard)


print("------------------ Order data -----------------")
print(f"Order id = {my_order.getId()}")
print(f"Customer name = {my_order.getCustomer().getName()}")
print(f"Order date = {my_order.getOrderDate()}")
print(f"Order Total = {my_order.getOrderTotal()}")
print("------------------- Order Items List Lines --------------------")

for item in my_order.getItems():
    print("--------------")
    print(f"line nbr = {item.getLineNbr()}")
    print(f"Product name = {item.getProduct().getName()}")
    print(f"Quantity = {item.getQuantity()}")
    print(f"Unit price = {item.getUnitPrice()}")
    print(f"item tax = {item.getTax()}")
    print(f"item total = {item.getItemTotal()}")




