# Importing the libraries 
import requests # To get data from the internet via APIs
import smtplib # To send email through python
from email.message import EmailMessage

API_KEY = "adb128fc22d3c9cd2a59e6de845bc96b"
API_END_POINT = "https://api.openweathermap.org/data/2.5/onecall"
 
# ------------- Weather Parameters -------------------- #
weather_params = {
    "lat" :  22.5726,
    "lon" : 88.3639,
    "appid" : API_KEY,
    "exclude" : "minutely,daily,alerts"
}

# ------------------ Getting The Response ----------------- #
response = requests.get(API_END_POINT, params = weather_params)

response.raise_for_status()

weather_data = response.json()

# ------------------ GETTING THE DATA -------------------------------- #
curr_temp = round(weather_data['current']['temp']) - 273
feels_like = round(weather_data['current']['feels_like']) - 273
wind_speed = weather_data['current']['wind_speed']
desc = weather_data['current']['weather'][0]['description']
# ------- Checking for Rain ---------- #
weather_slice = weather_data['hourly'][:12]

for hour_data in weather_slice:
    condition = hour_data['weather'][0]['id']
    if int(condition) < 600:
        will_rain = "It's gonna rain today. Take an Umbrella."
        break
    else:
        will_rain = "It's not going to be a rainy day. ;)"

# ------- Data to be sent ---------- #
data = f" {will_rain}\n\n Today's Temperature : {curr_temp}°C \n\n Temperature Feels Like : {feels_like}°C \n\n Today's Wind Speed : {wind_speed} \n\n Over all Weather description : {desc}"

# -------------------------------------------- Mail ------------------------------------------- #
my_email = "williamskyle336@gmail.com"
password = "sayaN@79sarkar"

# ----------------- Creating the Connection ---------------- #
connection = smtplib.SMTP_SSL("smtp.gmail.com", 465)
connection.login(my_email, password)
# ------------ Sending related INFOs ------------- #
msg = EmailMessage()
msg['Subject'] = "!!!!!! Today's Weather Update !!!!!!"
msg['From'] = my_email
msg['To'] = "williamskyle562@gmail.com"
msg.set_content(data)

connection.send_message(msg) # Sedning the Message
connection.quit() # Ending the connection
