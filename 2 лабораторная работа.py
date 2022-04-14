import requests
def main():
    city = 'Moscow,RU'
    appid = '84bfc5f42c5b45d8bdb782bcc1d77cac'
    res = requests.get('http://api.openweathermap.org/data/2.5/forecast',
                       params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
    data = res.json()
    print('Прогноз погоды на неделю:')
    for i in data['list']:
        print('Дата:',i['dt_txt'],
              '\nТемпература:',i['main']['temp'],'°C'
              '\nПогодные условия:',i['weather'][0]['description'],
              '\nСкорость ветра:',i['wind']['speed'],'м/с'
              '\nВидимость:',i['visibility'],'метров')
if __name__ == '__main__':
    main()