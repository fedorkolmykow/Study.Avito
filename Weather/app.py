# app.py
import requests
import configparser
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_name():

    return

@app.route('/forecast/')
def get_forec_weather():
    #Получение названия города
    city = request.args.get("city")
    if city is None:
        return "Передайте через параметр city название города, в котором требуются узнать погоду."
    #Получение времени прогноза
    hours = request.args.get("dt")
    if hours is None:
        return "Передайте через параметр dt количество часов, после которых нужен прогноз."
    #Чтение url из конфигурационного файла
    conf = configparser.RawConfigParser()
    conf.read("weatherUrl.conf")
    url = conf.get("url", "forecWeather") + 'city=' + city + '&hours=' + hours
    #Запрос на информацию о погоде и парсинг ответа
    r = requests.get(url)
    info = r.json()
    output = dict(city=info["city_name"], unit="celsius", temperature=(info["data"][int(hours) - 1])["temp"])
    return output


@app.route('/current/')
def get_cur_weather():
    #Получение названия города
    city = request.args.get("city")
    if city is None:
        return "Передайте через параметр city название города, в котором требуются узнать погоду."
    city = 'city=' + city
    #Чтение url из конфигурационного файла
    conf = configparser.RawConfigParser()
    conf.read("weatherUrl.conf")
    url = conf.get("url", "curWeather") + city
    #Запрос на информацию о погоде и парсинг ответа
    r = requests.get(url)
    info = r.json()
    output = dict(city=(info["data"][0])["city_name"], unit="celsius", temperature=(info["data"][0])["temp"])
    return output


if __name__ == '__main__':
    app.run(debug=True, port=5001, host="0.0.0.0")


