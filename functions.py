import datetime
import os

import bs4
import httplib2
import requests
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


def url_xml():
    x = datetime.datetime.now()
    day = x.strftime("%d")
    month = x.strftime("%m")
    year = x.strftime("%G")
    today = str(day) + "/" + str(month) + "/" + str(year)

    url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=' + str(today)
    return url


def get_service_sacc():
    creds_json = os.path.dirname(__file__) + "/key.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']

    creds_service = ServiceAccountCredentials.from_json_keyfile_name(creds_json, scopes).authorize(httplib2.Http())
    return build('sheets', 'v4', http=creds_service)


def exchange_rates(url_xml):
    url_code = requests.get(url_xml)
    soup = bs4.BeautifulSoup(url_code.text, 'lxml')

    char_code = soup.find_all('charcode')
    value = soup.find_all('value')
    currencies = []
    for i in range(0, len(char_code)):
        rows = [
            char_code[i].get_text(),
            value[i].get_text()]
        if char_code[i].get_text() == 'USD':
            currencies.append(rows)
    return currencies
