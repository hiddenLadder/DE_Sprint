from bs4 import BeautifulSoup
import requests as req
import json


data = {
    'data': []
}

pages = 1

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

for page in range(pages):
    url = f'https://hh.ru/search/vacancy?search_field=name&search_field=company_name&search_field=description&text=python+разработчик&from=suggest_post&page={page}'
    res = req.get(url=url, headers=headers)
    curr_page = BeautifulSoup(res.text, 'lxml')
    vacancies = curr_page.find_all(class_='serp-item')
    for vacancy in vacancies:
        a_tag = vacancy.find(attrs={'data-qa': 'serp-item__title'})

        inner_url = a_tag.attrs['href']
        inner_res = req.get(inner_url, headers=headers)

        vacancy_page = BeautifulSoup(inner_res.text, 'lxml')

        title = a_tag.text
        region = vacancy.find(
            attrs={'data-qa': 'vacancy-serp__vacancy-address'}).text
        vacancy_experience = vacancy_page.find(
            attrs={'data-qa': 'vacancy-experience'}).text
        salary = vacancy_page.find(
            attrs={'data-qa': 'vacancy-salary'}).text

        data['data'].append(
            {'title': title, 'work experience': vacancy_experience, 'salary': salary, 'region': region})

with open('data.json', 'w', encoding='utf8') as file:
    json.dump(data, file, ensure_ascii=False)
