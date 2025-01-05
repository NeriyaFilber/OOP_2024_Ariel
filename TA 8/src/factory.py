from abc import ABC, abstractmethod


# Product interface
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


# Concrete products
class CreditCardPayment(Payment):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing credit card payment of ${amount}")
        # Add credit card processing logic here
        return True


class PayPalPayment(Payment):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing PayPal payment of ${amount}")
        # Add PayPal processing logic here
        return True


class CryptoPayment(Payment):
    def process_payment(self, amount: float) -> bool:
        print(f"Processing cryptocurrency payment of ${amount}")
        # Add cryptocurrency processing logic here
        return True


# Simple Factory
class PaymentFactory:
    @staticmethod
    def create_payment(payment_method: str) -> Payment:
        """Simple factory method to create payment objects"""
        if payment_method.lower() == "credit":
            return CreditCardPayment()
        elif payment_method.lower() == "paypal":
            return PayPalPayment()
        elif payment_method.lower() == "crypto":
            return CryptoPayment()
        else:
            raise ValueError(f"Unsupported payment method: {payment_method}")


# Creator (Abstract Factory)
class PaymentProcessor(ABC):
    @abstractmethod
    def create_payment(self) -> Payment:
        """Factory method"""
        pass

    def process_order(self, amount: float) -> bool:
        """Template method that uses the factory method"""
        payment = self.create_payment()

        # Perform some validation
        if amount <= 0:
            raise ValueError("Amount must be positive")

        # Process the payment
        return payment.process_payment(amount)


# Concrete Creators
class CreditCardProcessor(PaymentProcessor):
    def create_payment(self) -> Payment:
        return CreditCardPayment()


class PayPalProcessor(PaymentProcessor):
    def create_payment(self) -> Payment:
        return PayPalPayment()


class CryptoProcessor(PaymentProcessor):
    def create_payment(self) -> Payment:
        return CryptoPayment()


# Client code
def process_customer_payment(payment_type: str, amount: float):
    """Example of using the simple factory"""
    try:
        # Using simple factory
        payment = PaymentFactory.create_payment(payment_type)
        result = payment.process_payment(amount)
        print(f"Payment processed successfully: {result}\n")
    except ValueError as e:
        print(f"Error: {e}\n")


def process_with_processor(processor: PaymentProcessor, amount: float):
    """Example of using the factory method pattern"""
    try:
        result = processor.process_order(amount)
        print(f"Order processed successfully: {result}\n")
    except ValueError as e:
        print(f"Error: {e}\n")


# Example usage
def main():
    # Using simple factory
    print("=== Using Simple Factory ===")
    process_customer_payment("credit", 100.00)
    process_customer_payment("paypal", 50.00)
    process_customer_payment("crypto", 75.00)

    # Using factory method pattern
    print("=== Using Factory Method Pattern ===")
    processors = [
        CreditCardProcessor(),
        PayPalProcessor(),
        CryptoProcessor()
    ]

    for processor in processors:
        process_with_processor(processor, 100.00)


if __name__ == "__main__":
    main()
