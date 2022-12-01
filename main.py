from pyqiwip2p import QiwiP2P
from pyqiwip2p.p2p_types import QiwiCustomer, QiwiDatetime, PaymentMethods
import random

QIWI_PRIV_KEY = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6InAzbGdpMC0wMCIsInVzZXJfaWQiOiI3OTY2MDg1OTcxOSIsInNlY3JldCI6ImUyZTc0MjQxZjU0ZTFhOWE2N2E1MGM3ZmYzNThlZDA1Y2U5Mjg3YmJhYThmOWQ4ZDVlNmIwMzkxMDg2Yzk5NTAifX0="

p2p = QiwiP2P(auth_key=QIWI_PRIV_KEY)

# Выставим счет на сумму 228 рублей который будет работать 45 минут
new_bill = p2p.bill(bill_id=random.randint, amount=0.1, lifetime=1)

print(new_bill.bill_id, new_bill.pay_url)

