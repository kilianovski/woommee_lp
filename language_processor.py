import pymorphy2
import io
import requests
import datetime
import json

CITIES_URI = "https://raw.githubusercontent.com/mitutee/woommee_wp/master/pure_cities.txt"
WOOMMEE_WP_URI = "http://mitutee.tech:8888/api"
CITIES = requests.get(CITIES_URI).text.lower().split()


morph = pymorphy2.MorphAnalyzer()

default = 'Oops v_o__0_V       Something is wrong'

def get_answer(user, question):
    try:
        question_tokens = question.split()
    except AttributeError as e:
        return default
    
    if 'погода' in morph.normal_forms(question_tokens[0]):
        word1 = morph.normal_forms(question_tokens[1])[0]
        if len(question_tokens ) > 2 and morph.normal_forms(question_tokens[2])[0] in CITIES:
            weather = getWeather(morph.normal_forms(question_tokens[2])[0])
        elif word1 in CITIES:
            weather = getWeather(word1)
        else:
            return "No such city"
        daily = weather["daily"]
        date = datetime.datetime.fromtimestamp(int(daily["data"][0]["time"])).strftime('%Y-%m-%d %H:%M:%S')
        answer = "Погода в {0} на {1} : {2}.".format(weather["_city"], date, daily['summary'])
        return answer
    else :
        return default


def getWeather(city):
    res = requests.get("{}/{}".format(WOOMMEE_WP_URI, city)).text
    raw = json.loads(res)
    raw["_city"] = city
    return raw
    


print(get_answer("asdf",'погода в Киеве'))
