import requests
from datetime import datetime

key = "5d6e97c7b2db4ada84e161243242911"  # TODO подставить ваш ключ к API
lat = "59.93"  # широта в градусах
lon = "30.31"  # долгота в градусах

url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={lat},{lon}"
response = requests.get(url)  # отправление GET запроса и получение ответа от сервера
print(response.json())  # получение JSON из ответа

# Словарь перевода значений направления ветра
DIRECTION_TRANSFORM = {
    'n': 'северное',
    'nne': 'северо - северо - восточное',
    'ne': 'северо - восточное',
    'ene': 'восточно - северо - восточное',
    'e': 'восточное',
    'ese': 'восточно - юго - восточное',
    'se': 'юго - восточное',
    'sse': 'юго - юго - восточное',
    's': 'южное',
    'ssw': 'юго - юго - западное',
    'sw': 'юго - западное',
    'wsw': 'западно - юго - западное',
    'w': 'западное',
    'wnw': 'западно - северо - западное',
    'nw': 'северо - западное',
    'nnw': 'северо - северо - западное',
    'c': 'штиль',
}


def current_weather(lat, lon):
    """
    Описание функции, входных и выходных переменных
    """
    key = "5d6e97c7b2db4ada84e161243242911"  # TODO подставить ваш ключ к API
    url = f"https://api.weatherapi.com/v1/current.json?key={key}&q={lat},{lon}"
    # то вместо forecast используйте informers. url = f"https://api.weather.yandex.ru/v2/informers?lat={lat}&lon={lon}"
    # headers = {"X-Yandex-API-Key": f"{token}"}
    # response = requests.get(url, headers=headers)
    response = requests.get(url)
    data = response.json()

    # Данная реализация приведена для тарифа «Тестовый», если у вас Тариф «Погода на вашем сайте», то закомментируйте пару строк указанных ниже
    result = {
        'city': data['location']['name'],  # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
        'time': datetime.fromtimestamp(data[['current']]['last_updated']).strftime("%H:%M"),  # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
        'temp': ['current']['temp_c'],  # TODO Реализовать вычисление температуры из данных полученных от API
        'feels_like_temp': ['current']['feelslike_c'],  # TODO Реализовать вычисление ощущаемой температуры из данных полученных от API
        'pressure': ['current']['pressure_mb'],  # TODO Реализовать вычисление давления из данных полученных от API
        'humidity': ['current']['humidity'],  # TODO Реализовать вычисление влажности из данных полученных от API
        'wind_speed': ['current']['wind_kph'],  # TODO Реализовать вычисление скорости ветра из данных полученных от API
        'wind_gust': ['current']['gust_kph'],  # TODO Реализовать вычисление скорости порывов ветка из данных полученных от API
        'wind_dir': DIRECTION_TRANSFORM.get(data['current']['wind_dir']),  # Если используете Тариф «Погода на вашем сайте», то закомментируйте эту строку
    }
    return result


if __name__ == "__main__":
    print(current_weather(59.93, 30.31))  # Проверка работы для координат Санкт-Петербурга
