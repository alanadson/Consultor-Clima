import requests
import json
import time
import datetime
from translate import Translator
import translate

cidade = input('Digite sua cidade: ') 
req = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=9676e7fa61747b175b2a5717bed4a03b')

tempo = json.loads(req.text)

try:
  s = Translator(to_lang="portuguese")
  res = s.translate(tempo['weather'][0]['main'])
  print('Condicao do tempo:', res)
  tempC = float(tempo['main']['temp'] - 273.15) 
  print('Temperatura:', format(tempC, '.2f'))

except:
  print('Cidade nao encontrada')