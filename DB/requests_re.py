import requests
from peewee import SqliteDatabase, Model, DoubleField, CharField, DateTimeField
import datetime
import xml.etree.cElementTree as ElT

db = SqliteDatabase('xrates.db')


class XRate(Model):
    class Meta:
        database = db
        db_table = "xrates"

    from_currency = CharField()
    to_currency = CharField()
    rate = DoubleField()
    write_datetime = DateTimeField()

    def __str__(self):
        return f"Rate {self.from_currency} => {self.to_currency}: {'{:.8f}'.format(self.rate)}"


def get_pb_rates():

    response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")

    json_resp = response.json()

    result = [(info["ccy"], info["base_ccy"], info["sale"])
              for info in json_resp]

    return result


def get_cbr_rates():
    response = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    root = ElT.fromstring(response.text)

    result = [(itm.find("CharCode").text, itm.find("Nominal").text, itm.find("Value").text) for itm in root]

    return result


if __name__ == '__main__':

    XRate.create_table()

    # rates from privat
    rate_info = get_pb_rates()

    # create or update BD
    for from_currency, to_currency, rate in rate_info:

        selected_row = XRate.get_or_none((XRate.from_currency == from_currency) & (XRate.to_currency == to_currency))

        if selected_row:
            selected_row.rate = rate
            selected_row.write_datetime = datetime.datetime.now()
            selected_row.save()
        else:
            XRate.create(from_currency=from_currency.upper(),
                         to_currency=to_currency.upper(),
                         rate=rate,
                         write_datetime=datetime.datetime.now())

    rates = XRate.select()
    for item in rates:
        print(item)
    # get rates from cbr
    rate_info = get_cbr_rates()
    # create or update BD
    to_currency = "RUR"
    for from_currency, nominal, rate in rate_info:
        selected_row = XRate.get_or_none((XRate.from_currency == from_currency) & (XRate.to_currency == to_currency))

        if selected_row:
            selected_row.rate = round(float(rate.replace(",", ".")) / int(nominal), 8)
            selected_row.write_datetime = datetime.datetime.now()
            selected_row.save()
        else:
            XRate.create(from_currency=from_currency.upper(),
                         to_currency=to_currency.upper(),
                         rate=round(float(rate.replace(",", ".")) / int(nominal), 8),
                         write_datetime=datetime.datetime.now())
    print("--------------------------")
    rates = XRate.select()
    for item in rates:
        print(item)

    db.close()
