from tkinter import *
import tkinter as tk

from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import time
import pytz
 
def getWeather(canvas):
    city=textfield.get()
    api="https://api.openweathermap.org/data/2.5/weather?q=" + city +"&appid=b4c22ec5fc9b3babba3c9b822e5cec19"
    json_data=requests.get(api).json()
    condition=json_data['weather'][0]['main']
    temp=int(json_data['main']['temp'] -273.14)
    min_temp=int(json_data['main']['temp_min'] -273.14)
    max_temp=int(json_data['main']['temp_max'] -273.14)
    pressure=json_data['main']['pressure']
    humidity=json_data['main']['humidity']
    wind=json_data['wind']['speed']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-19800))
    sunset=time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-19800))
    
    final_info =condition + "\n" +str(temp) + "C"
    final_data ="\n" +"Max Temp: " + str(max_temp) + "\n" +"Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) +"\n" + "Humidity: " + str(humidity) + "\n"+ "Wind Speed: " + str(wind) +"\n" +"Sunrise: " + sunrise +"\n"+ "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)
    

canvas =tk.Tk()
canvas.geometry("800x600")
canvas.title("Weather App") 

f=("poppins",15,"bold")
t=("poppins",35,"bold")

textfield=tk.Entry(canvas,font= t)
textfield.pack(pady=30)
textfield.focus()
textfield.bind('<Return> ',getWeather)

label1=tk.Label(canvas,font= t)
label1.pack()
label2=tk.Label(canvas,font= f)
label2.pack()

canvas.mainloop()
