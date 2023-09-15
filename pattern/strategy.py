# Define a family of algorithms

class PaymentStrategy:
    def pay(self, amount):
        pass

# Concrete Strategy 1
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with Credit Card")

# Concrete Strategy 2
class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with PayPal")

# Context
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.items = []
        self.payment_strategy = payment_strategy

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item['price'] for item in self.items)

    def checkout(self):
        total = self.calculate_total()
        self.payment_strategy.pay(total)

# Client code
if __name__ == "__main__":
    credit_card_payment = CreditCardPayment()
    paypal_payment = PayPalPayment()

    cart1 = ShoppingCart(credit_card_payment)
    cart1.add_item({"item": "Product A", "price": 100})
    cart1.add_item({"item": "Product B", "price": 50})
    cart1.checkout()

    cart2 = ShoppingCart(paypal_payment)
    cart2.add_item({"item": "Product C", "price": 75})
    cart2.checkout()
