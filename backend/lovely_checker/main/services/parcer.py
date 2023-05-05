import time
import random

from django.contrib.auth.models import User
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

from item.models import Item, Comment, CategoryItem


def parse_yandex(city_t):
        # Настройки Selenium
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-infobars')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3')
        driver = webdriver.Chrome(options=options)
        # city = input('Введите город: ')
        city = city_t[0].code
        user = User.objects.get(id=1)
        categorys = ['кафе', 'парки', 'отели', 'кино']  # Задаем категорию объектов
        categorys_en = [CategoryItem.objects.get(name='Cafe/Restaurant'),
                        CategoryItem.objects.get(name='Parks/Squares'),
                        CategoryItem.objects.get(name='Hotel'),
                        CategoryItem.objects.get(name='Theatre/Cinema')]
        print(categorys_en)# Задаем категорию объектов
        for category_en, category_rus in enumerate(categorys):
            # Запуск браузера
            driver.get(f'https://yandex.ru/maps/{city}/smt/?text={category_rus}')

            # Рандомизация интервалов между запросами
            time.sleep(random.uniform(1, 3))

            # Получение HTML-кода страницы
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            # Найти все метки на карте
            marks = soup.find_all('li', {'class': 'search-snippet-view'})
            for mark in marks:
                # Извлечь имя объекта
                name = mark.find('div', {'class': 'search-business-snippet-view'}) \
                    .find('div', {'class': 'search-business-snippet-view__title'}).text.strip()

                # Извлечь описание объекта
                address = mark.find('div', {'class': 'search-business-snippet-view__address'}).text.strip()
                address_link = f"https://yandex.ru{mark.find('a', {'class': 'search-snippet-view__link-overlay'}).get('href')}"
                driver.get(address_link)

                item = Item.objects.get_or_create(
                    title=name,
                    city=city_t[0],
                    category=categorys_en[category_en],
                    author=user,
                    description='',
                    address=address,
                    address_link=f"https://yandex.ru{address_link}"
                )
                # Извлечь отзывы объекта
                driver.find_element("class name", "_name_reviews").click()
                # скрол для добавления отзывов
                time.sleep(random.uniform(2, 4))
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
                try:
                    time.sleep(random.uniform(2, 4))
                    target = driver.find_element("class name", "business-reviews-card-view__skeletons")
                    actions = ActionChains(driver)
                    actions.move_to_element(target)
                    actions.perform()
                except NoSuchElementException:
                    pass
                current_object_reviews = BeautifulSoup(driver.page_source, 'html.parser')

                reviews = current_object_reviews.find_all('div', {'class': 'business-review-view__info'})
                reviews_des = []
                for r in reviews:
                    rating = len(
                        r.find('div', {'class': 'business-rating-badge-view__stars'}).find_all('span', {'class': '_full'}))
                    description = r.find('span', {'class': 'business-review-view__body-text'}).text.strip()
                    reviews_des.append({rating: description})
                    Comment.objects.create(
                        description=description,
                        rating=rating,
                        item=item[0],
                        author=user
                    )
                # Рандомизация интервалов между запросами
                time.sleep(random.uniform(2, 5))

            # Закрытие браузера
            driver.quit()


# class Client:
#
#     API_URL = "https://geocode-maps.yandex.ru/1.x/"
#     PARAMS = {"format": "json"}
#
#     @classmethod
#     def request(cls, address: str) -> dict:
#         response = requests.get(
#             cls.API_URL, params=dict(geocode=address, **cls.PARAMS)
#         )
#
#         if response.status_code != 200:
#             raise Exception(
#                 "Non-200 response from yandex geocoder"
#             )
#
#         return response.json()["response"]
#
#     @classmethod
#     def coordinates(cls, address: str) -> typing.Tuple[str, str]:
#         data = cls.request(address)["GeoObjectCollection"]["featureMember"]
#
#         if not data:
#             raise Exception(
#                 '"{}" not found'.format(address)
#             )
#
#         coordinates = data[0]["GeoObject"]["Point"]["pos"]  # type: str
#         print(data)
#         print(data[0]["GeoObject"])
#         return tuple(coordinates.split(" "))
#
# Client.request(address='Тургеневский переулок, 24, Таганрог, Ростовская область')