from view.view import View
from model.model import Weather


class Controller:

    def __init__(self) -> None:
        self.view = View(self)
        self.weather = Weather()
        self.update_gui()

    def main(self):
        self.view.main()

    def update_gui(self):
        try:
            if 'Error' not in self.weather.weather_data:
                self.view.var_location.set(self.weather.get_loc())
                self.view.var_conditions.set(self.weather.get_cond_text())
                self.view.var_wind_speed.set(self.weather.get_wind_speed_k())
                self.view.var_wind_direction.set(self.weather.get_wind_dir())

                if self.view.var_unit.get() == 1:
                    self.view.var_temp.set(self.weather.get_curr_temp_farhen())
                    self.view.var_feels_like.set(
                        self.weather.get_feels_like_f())

                else:
                    self.view.var_temp.set(
                        self.weather.get_curr_temp_celsius())
                    self.view.var_feels_like.set(
                        self.weather.get_feels_like_c())

        except:
            pass

    def handle_button_search(self, event=None):
        location = self.view.var_search.get()
        if location != '':
            self.weather = Weather(location)
            self.update_gui()
