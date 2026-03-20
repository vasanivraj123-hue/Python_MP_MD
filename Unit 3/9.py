from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        """Must be implemented by subclasses"""
        pass

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing ${amount} via PayPal.")

class CheckoutSystem:
    def __init__(self, processor: PaymentProcessor):
        self.processor = processor

    def complete_purchase(self, total: float):
        print("Finalising order...")
        self.processor.process_payment(total)

paypal = PayPalProcessor()
checkout = CheckoutSystem(paypal)
checkout.complete_purchase(50.0)
