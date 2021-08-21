import requests

class Weather:
    def __init__(self, location="Kolkata"):
        self.weather_data = {}
        self.fetch(location)
        
    def get_loc_data(self, name):
        data = self.weather_data['location'][name]
        return str(data)
    
    def get_city(self):
        return self.get_loc_data('name')
    
    def get_state(self):
        return self.get_loc_data('region')
    
    def get_country(self):
        return self.get_loc_data('country')
    
    def get_time_zone(self):
       return self.get_loc_data('tz_id')
    
    def get_loc(self):
        if 'Aisa' in self.get_time_zone():
            return f"{self.get_city()}, {self.get_state()}"
        else:
            return f"{self.get_city()}, {self.get_country()}"
        
    def get_curr_data(self, name):
        data = self.weather_data['current'][name]
        return data if name == 'condition' else str(data)
    
    def get_cond_text(self):
        condition = self.get_curr_data('condition')
        return str(condition['text'])
    
    def get_curr_temp_farhen(self):
        return self.get_curr_data("temp_f")
    
    def get_curr_temp_celsius(self):
        return self.get_curr_data("temp_c")
    
    def get_feels_like_c(self):
        return self.get_curr_data("feelslike_c")
    
    def get_feels_like_f(self):
        return self.get_curr_data("feelslike_f")
    
    def get_wind_speed_m(self):
        return self.get_curr_data("wind_mph")
    
    def get_wind_speed_k(self):
        return self.get_curr_data("wind_kph")
    
    def get_wind_dir(self):
        return self.get_curr_data("wind_dir")
    
    def fetch(self, query):
        try:
            API_KEY = 'fab91458d72d4c26968164028211908' # Api key 
            URL = f"http://api.weatherapi.com/v1/current.json" + \
                f"?key={API_KEY}&q={query}&aqi=no"
            self.weather_data = requests.get(URL).json()
            
        except:
            self.weather_data = {'Error'}
    