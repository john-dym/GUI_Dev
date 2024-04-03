#P3 - Catering App
#Author: John Morales - https://github.com/john-dym
#Class: GUI Development

from decimal import Decimal
class platter_item:

    def __init__(self, name, price):
        self.name = name
        self.price = Decimal(price).quantize(Decimal('1.00'))

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name

