#!/usr/bin/python3
# -*- coding: utf-8 -*-

import requests

while True:
  city = input("请输入城市，回车退出:\n")
  if not city:
    break
  try:
    req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
  except:
    print("请求失败\n")
    break
  dict_city = req.json()
  city_data = dict_city.get('data')
  if city_data:
    city_forecast = city_data['forecast'][0]
    print(city_forecast.get('date'))
    print(city_forecast.get('high'))
    print(city_forecast.get('low'))
    print(city_forecast.get('type'))
  else:
    print("未获得")
