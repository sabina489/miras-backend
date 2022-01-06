from payments.gateways.base import BasicGateway


from ..base import BasicGateway

from payments import PaymentStatus


class KhaltiGateway(BasicGateway):
    def capture(self, payment, amount, ref_id):
        pass

    def verify():
        pass
