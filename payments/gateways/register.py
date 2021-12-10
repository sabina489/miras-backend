from .factory import GatewayFactory
from esewa.pay import EsewaGateway


gateway_factory = GatewayFactory()

gateway_factory.register('ESEWA', EsewaGateway)