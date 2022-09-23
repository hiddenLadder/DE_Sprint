from requests_tor import RequestsTor
from bs4 import BeautifulSoup
import requests as req

url = 'https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=python+разработчик&from=suggest_post'

res = req.get(url)
print(res)
