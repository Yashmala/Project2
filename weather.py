from tkinter import *
from tkinter import ttk
import pip._vendor.requests
#in this we will need the data to transmit to servers and thereby fetch the information from there 
# so we would be taking weather api from openweathermap.org
#An application programming interface (API) is a way for two or more computer programs to communicate with each other. It is a type of software interface, offering a service to other pieces of software.
#so to communicate between our software and the weather server for weather info we have to use api
#in order to use api in python we need to use a "request" package this helps to run the api i.e it hits the url 
def get_fun():
    city=city_name.get() # this will get the name of city from tkinter command
    data=pip._vendor.requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=41b7c407d06a92ee959e5dd9220f4cdb").json()
    # this are all the text labels in which all will give the result of all these values
    weather_climate1.config(text=data["weather"][0]["main"])
    weather_description1.config(text=data["weather"][0]["description"])
    temp1.config(text=str(int(data["main"]["temp"]-273.15)))
    temp_min1.config(text=str(int(data["main"]["temp_min"]-273.15)))
    temp_max2.config(text=str(int(data["main"]["temp_max"]-273.15)))
    presure1.config(text=data["main"]["pressure"])
    humidity1.config(text=str(data["main"]["humidity"]))
    sea_level1.config(text=str(data["main"]["sea_level"]))
    ground_level1.config(text=str(data["main"]["grnd_level"]))





root=Tk()

root.title(" PYTHON APPLICATION")
root.config(bg= "royal blue")
root.geometry("800x800")
nlabel1=Label(root,text="WEATHER FORECASTING APP",font=("Time New Roman",20,"bold"))
nlabel1.place (x=150,y=30,height=50,width=450)


# creating gui for app 
city_name=StringVar()
combo1=ttk.Combobox(root,text=" WEATHER FORECASTING APP",font=("Time New Roman",20,"bold"),textvariable=city_name)
combo1.place (x=175,y=120,height=50,width=400)
# combo used for a drop box giving multiple options which can be further modified 

# labels created for getting results of weather
weather_climate=Label(root,text="  CLIMATE: ",font=("Time New Roman",10,"bold"))
weather_climate.place(x=175,y=400,height=30,width=200)
weather_climate1=Label(root,text="   ",font=("Time New Roman",10,"bold"))
weather_climate1.place(x=400,y=400,height=30,width=200)
weather_description=Label(root,text=" DESCRIPTION: ",font=("Time New Roman",10,"bold"))
weather_description.place(x=175,y=450,height=30,width=200)
weather_description1=Label(root,text=" ",font=("Time New Roman",10,"bold"))
weather_description1.place(x=400,y=450,height=30,width=200)
temp=Label(root,text=" TEMPERATURE: ",font=("Time New Roman",10,"bold"))
temp.place(x=175,y=500,height=30,width=200)
temp1=Label(root,text="  ",font=("Time New Roman",10,"bold"))
temp1.place(x=400,y=500,height=30,width=200)

temp_min=Label(root,text=" MINIMUM TEMPERATURE : ",font=("Time New Roman",10,"bold"))
temp_min.place(x=175,y=550,height=30,width=200)
temp_min1=Label(root,text=" ",font=("Time New Roman",10,"bold"))
temp_min1.place(x=400,y=550,height=30,width=200)
temp_max=Label(root,text=" MAXIMUM TEMPERATURE: ",font=("Time New Roman",10,"bold"))
temp_max.place(x=175,y=600,height=30,width=200)
temp_max2=Label(root,text=" ",font=("Time New Roman",10,"bold"))
temp_max2.place(x=400,y=600,height=30,width=200)
presure=Label(root,text=" PRESSURE: ",font=("Time New Roman",10,"bold"))
presure.place(x=175,y=650,height=30,width=200)
presure1=Label(root,text=" ",font=("Time New Roman",10,"bold"))
presure1.place(x=400,y=650,height=30,width=200)
humidity=Label(root,text=" HUMIDITY: ",font=("Time New Roman",10,"bold"))
humidity.place(x=175,y=700,height=30,width=200)
humidity1=Label(root,text=" ",font=("Time New Roman",10,"bold"))
humidity1.place(x=400,y=750,height=30,width=200)
sea_level=Label(root,text=" SEA LEVEL: ",font=("Time New Roman",10,"bold"))
sea_level.place(x=175,y=750,height=30,width=200)
sea_level1=Label(root,text=" ",font=("Time New Roman",10,"bold"))
sea_level1.place(x=400,y=800,height=30,width=200)
ground_level=Label(root,text=" GROUND LEVEL: ",font=("Time New Roman",10,"bold"))
ground_level.place(x=175,y=800,height=30,width=200)
ground_level1=Label(root,text=" ",font=("Time New Roman",10,"bold"))
ground_level1.place(x=400,y=700,height=30,width=200)
b1=Button(root,text=" SEARCH",font=("Time New Roman",20,"bold"),command=get_fun)
b1.place(x=300,y=200,height=50,width=150)
# button created for searching the weather for given location 
root.mainloop()