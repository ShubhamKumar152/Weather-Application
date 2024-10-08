from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
# root.configure(bg = "#57adff") #BackgroundColour
root.resizable(False,False)

def getWeather():
    try:
        city=textfield.get()

        geolocator= Nominatim(user_agent= "geoapiExercises")
        location= geolocator.geocode(city)
        

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #Weather
        api="https://api.openweathermap.org/data/2.5/weather"
        params = {
            "lat": location.latitude,
            "lon": location.longitude,
            "appid": "a444939bbd32e459e0fbfcb14522b518"
        }
        response = requests.get(api, params=params)
        json_data = response.json()
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp']-273.15)
        pressure = json_data['main']['pressure']            
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")



# Search Box
Search_image=PhotoImage(file="Weather app images/search.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=20)

textfield=tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"),bg="#404040",border=0, fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="Weather app images/search_icon.png")
myimage_icon=Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400,y=34)


#Logo
Logo_image=PhotoImage(file="Weather app images/logo.png")
logo=Label(image=Logo_image)
logo.place(x=150,y=100)


#Bottom Box
Frame_image=PhotoImage(file="Weather app images/box.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)


#Time
name=Label(root,font=("arial", 15, "bold"))
name.place(x=30,y=100)
clock=Label(root,font=("Helvetica", 20))
clock.place(x=30,y=130)


#Label
Label1=Label(root,text="WIND",font=("Helvetica", 15, "bold"), fg="White", bg="#1ab5ef")
Label1.place(x=120,y=400)

Label2=Label(root,text="HUMIDITY ",font=("Helvetica", 15, "bold"), fg="White", bg="#1ab5ef")
Label2.place(x=250,y=400)

Label3=Label(root,text="DESCRIPTION",font=("Helvetica", 15, "bold"), fg="White", bg="#1ab5ef")
Label3.place(x=430,y=400)

Label4=Label(root,text="PRESSURE",font=("Helvetica", 15, "bold"), fg="White", bg="#1ab5ef")
Label4.place(x=650,y=400)



t=Label(font=("arial", 70, "bold"),fg="#ee666d")     #Temperature
t.place(x=400,y=150)

c=Label(font=("arial", 15, "bold"))                    #Condition
c.place(x=400,y=250)

w=Label(text="...",font=("arial", 20, "bold"),bg="#1ab5ef")      #Wind
w.place(x=120,y=430)

h=Label(text="...",font=("arial", 20, "bold"),bg="#1ab5ef")      #Humidity
h.place(x=280,y=430)

d=Label(text="...",font=("arial", 20, "bold"),bg="#1ab5ef")      #Description
d.place(x=450,y=430)

p=Label(text="...",font=("arial", 20, "bold"),bg="#1ab5ef")      #Pressure
p.place(x=670,y=430)





root.mainloop()