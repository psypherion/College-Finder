# ------ Importing Libraries ----- #
from tkinter import *
from tkinter import messagebox
import requests
from controller.controller import Controller
from model.model import Weather


def get_weather():
    if __name__=='__main__':
        Controller().main()
        
        
class NewsApp:

    def __init__(self, app):
        self.app = app
        self.app.title("News App")
        self.app.geometry("1470x800")

        # ---- Variables --- #
        self.new_cat = ["general", "entertainment", "business",
                       "sports", "technology", "health", "science"]  # Catagories of our News App
        self.news_cat_buttons = []

        # ---- GUI --- #
        bg_color = "#1a3300"  # Setting the Back ground colour of the App
        button_color = '#356600'  # Setting the button colors
        font_color = 'white'  # Setting the font colors

        Label(self.app, text="News App",
              font=('comics sans', 30),
              bg=bg_color,
              fg=font_color,
              relief=GROOVE,
              pady=2, bd=12).pack(fill=X)
        
        categories = LabelFrame(self.app,
                                text="Category",
                                font=('comics sans', 20, 'bold'),
                                bg=bg_color, fg=font_color,
                                relief=GROOVE, bd=10)
        categories.place(x=0, y=80, width=300, relheight=0.88)

        for i in range(len(self.new_cat)):
            buttons = Button(categories, text=self.new_cat[i].upper(),
                             font=('comics sans', 14, 'bold'),
                             bg=bg_color, fg=font_color,
                             bd = 7,
                             width=20, height=2,
                            )
            buttons.grid(row=i, column=0, padx=10, pady=5)
            buttons.bind('<Button-1>', self.news_area)
            self.news_cat_buttons.append(buttons)
        news = Frame(self.app, relief=GROOVE,
                     bd=7)
        news.place(x=320, y=80, relwidth=0.78, relheight=0.88)
        Label(news, text="News Area",
              bg=bg_color,
              fg=font_color,
              bd = 7, 
              relief=GROOVE,
              font=('comics sans', 20, 'bold')).pack(fill=X)
        scroll_y = Scrollbar(news, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.text_area = Text(news, 
                              yscrollcommand = scroll_y.set,
                              font=('Lora bold', 14),
                              bg=button_color,
                              fg=font_color)
        self.text_area.insert(
            END,
            "\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\n\t\t\t        PLEASE SELECT ANY CATEGORY TO SHOW HEADLINES AND \n\t\t\t PLEASE BE PATIENT, IT DEPENDS ON YOUR INTERNET CONNECTION")
        
        self.text_area.pack(fill='x')
        
        weather_button = Button(news, text="Check Weather".upper(),
                                font = ('rockwell bold', 14),
                                bg = "#444422", fg=font_color,
                                width=20,
                                bd=7,
                                command = get_weather
        )
        
        weather_button.place(x=0, y=625, relwidth=1, relheight=0.1)
        
        
    def news_area(self, event):
        TYPE = event.widget.cget('text').lower() # Type of News
        API_KEY = '82678f55a410470fa33d55b8b67c4c26' # Use your Api Key
        URL = f"https://newsapi.org/v2/top-headlines?country=in&category={TYPE}&apiKey={API_KEY}"
        
        self.text_area.delete("1.0", END)
        self.text_area.insert(END,
                              "\n Read the Latest News provided by NewsApp\n\n")
        self.text_area.insert(
            END, "--------------------------------------------------------------------\n\n")
        
        try:
            articles = (requests.get(URL).json())['articles']
            if articles != 0:
                for i in range(len(articles)):
                    self.text_area.insert(END, f"{articles[i]['title']}\n")
                    self.text_area.insert(
                        END, f"{articles[i]['description']}\n\n")
                    self.text_area.insert(END, f"{articles[i]['content']}\n\n")
                    self.text_area.insert(
                        END, f"read more... : {articles[i]['url']}\n")
                    self.text_area.insert(
                        END, "\n--------------------------------------------------------------------\n")
                    self.text_area.insert(
                        END, "--------------------------------------------------------------------\n\n")
            else:
                self.text_area.insert(END, "Sorry no News Available")
                
        except:
            messagebox.showerror(
                "ERROR", "Sorry! I can't connect to the Internet :( "
            )
        
        
app = Tk()
NewsApp(app)
app.mainloop()
