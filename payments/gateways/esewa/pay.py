from payments.gateways.base import BasicGateway


from ..base import BasicGateway

from payments import PaymentStatus

class EsewaGateway(BasicGateway):
    def capture(self, payment, amount):
        if payment.amount == amount:
            return PaymentStatus.PAID
            #TODO: Add payment verification
        else:
            return PaymentStatus.ERROR

    def verify():
        pass