from decimal import Decimal

_cdecFica = Decimal(0.0765)
_cdecFed = Decimal(0.22)
_cdecState = Decimal(0.04)

def calculate_state_tax(pay, rate=_cdecState):
    return Decimal(pay*rate).quantize(Decimal('1.00'))

def calculate_fica(pay, rate=_cdecFica):
    return Decimal(pay*rate).quantize(Decimal('1.00'))

def calculate_federal_tax(pay, rate=_cdecFed):
    return Decimal(pay*rate).quantize(Decimal('1.00'))

def calculate_net_income(pay):
    dec_pay = Decimal(pay).quantize(Decimal('1.00'))
    state_tax = calculate_state_tax(dec_pay)
    fica_amount = calculate_fica(dec_pay)
    fed_tax = calculate_federal_tax(dec_pay)
    net_income = dec_pay - (state_tax + fica_amount + fed_tax)
    return state_tax, fica_amount, fed_tax, net_income

def test_net_income():
    results = calculate_net_income(123456.78)
    for num in results:
        print(num)

if __name__ == '__main__':
    test_net_income()