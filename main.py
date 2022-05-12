from timeit import Timer
from email163 import send
import Weather
import laugh

city = Weather.city
nowTime = Weather.nowTime
weather = Weather.weather
tem = Weather.tem
notice = Weather.notice
time = Weather.time

print(city)
print(nowTime)
print(weather)
print(tem)
print(notice)
print(time)
text = city + '\n' + '\n' + nowTime + '\n' + '\n' + weather + '\n' + '\n' + tem + '\n' + '\n' + notice + '\n' + '\n' + time

send(text)
