class StripePayment:
    def pay(self, amount):
        print(f"pagamento de ${amount} via stripe processado.")


class PaypalPayment:
    def send_payment(self, amount):
        print(f"pagamento de ${amount} via Paypal processado.")


 

class PaypalAdapter(StripePayment): # Fixed indentation
    def __init__ (self, paypal_payment):
        self.paypal_payment = paypal_payment

    def pay(self, amount): #Fixed indentation
        self.paypal_payment.send_payment(amount)


def process_payment(payment_system, amount):
    payment_system.pay(amount) 



stripe_payment = StripePayment()
paypal_payment = PaypalAdapter(PaypalPayment())

process_payment(stripe_payment, 100) 
process_payment(paypal_payment, 200) 