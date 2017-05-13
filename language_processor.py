import pymorphy2
import io
with io.open('pure_cities.txt','r',encoding='utf8') as f:
    CITIES = f.read().split()
def get_answer(user, question):
    return question in CITIES