from functions import *
from models import *


url_xml = url_xml()
exchange_rates = exchange_rates(url_xml)
exchange_rates = exchange_rates[0][1].split(',')[0]


service = get_service_sacc()
sheet = service.spreadsheets()

sheet_id = "1zkXuv_L9u2bXxVvkxPFlUZZoRT2eg-Y7J8hzFRut8H4"

resp = sheet.values().get(spreadsheetId=sheet_id, range="Лист1!A2:D").execute()

all_values = resp['values']

for i in all_values:
    usd = i[2]
    ru = int(usd) * int(exchange_rates)
    i.append(ru)

    Data.create(
        order_number=i[1],
        price_usd=i[2],
        date=i[3],
        price_ru=i[4],
    )

