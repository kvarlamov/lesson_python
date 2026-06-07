from user_info_provider.address_provider.adressprovider import get_adress
from user_info_provider.number_provider.number_provider import get_number
import datetime
from datetime import date

print(f" Номер Олега: {get_number('Oleg')}")
print(f" Адресс Олега: {get_adress('Oleg')}")

# Пример работы со временем и датой:
# https://pythonru.com/primery/kak-ispolzovat-modul-datetime-v-python
dt_now = datetime.datetime.now()
print(f" Текущее время: {dt_now}")
current_date = date.today()
print(f"Текущая дата : {current_date}") 