from models import Payment
from app import log


def get_all_payments():
    payments = Payment.select().order_by(Payment.id.desc())
    return payments


def get_filtered_payments(args):
    pid = args.get("id")
    name = args.get("name")
    amount = args.get("amount")
    currency = args.get("currency")
    payments = Payment.select()

    if pid:
        payments = payments.where(Payment.id == pid)

    if name:
        payments = payments.where(Payment.name == name)

    if amount:
        payments = payments.where(Payment.amount == amount)

    if currency:
        payments = payments.where(Payment.currency == currency)

    return payments.order_by(Payment.id.desc())


def create_new_payment(request_data):
    request_data = dict(request_data.items())
    log.debug(request_data)
    new_payment = Payment.create(**request_data)
    return new_payment
