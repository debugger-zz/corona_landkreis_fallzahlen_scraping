from bs4 import BeautifulSoup

import requests
import datetime
import re

import locale
locale.setlocale(locale.LC_TIME, "de_DE.utf-8")

from database_interface import *

main_url = "https://www.landkreis-sigmaringen.de/de/Landratsamt/Kreisverwaltung/Fachbereiche/Gesundheit/Informationen-zum-neuartigen-Coronavirus"

req = requests.get(main_url)
bs = BeautifulSoup(req.text, "html.parser")

cases_pattern = "labordiagnostisch bestätigte Infektionen: [0-9]+ Personen"


# todo find status
#status_raw = re.findall("Stand: .* 2020", bs.findAll(text=re.compile("Stand: "))[0])[0]
# todo: parse time, non-zero padded 8:00 Uhr
#status= datetime.datetime.strptime(status_raw, 'Stand: %d. %B %Y').strftime("%Y-%m-%d")



cases_raw = re.findall(cases_pattern,bs.getText())[0]

cases = int(re.findall(r'[0-9]+', cases_raw)[0])

print(cases)
#add_to_database("Heilbronn", status, cases)
