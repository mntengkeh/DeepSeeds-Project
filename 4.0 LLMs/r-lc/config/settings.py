import requests
import os
from pprint import pprint
# from dotenv import load_dotenv

# load_dotenv()

def environmental_variables():
    import os
    from dotenv import load_dotenv, find_dotenv
    load_dotenv(find_dotenv())
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def load_google_llm():
    from langchain_google_genai import GoogleGenerativeAI
    environmental_variables()
    google_llm = GoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.6
    )
    return google_llm

def load_google_chat_model():
    from langchain_google_genai import ChatGoogleGenerativeAI
    environmental_variables()
    google_chat_model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.7
    )
    return google_chat_model



# weather api endpoint config

class WeatherAPILoader:
    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key

    #load data(live)
    def load(self):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metrics"
        weather_info = requests.get(url).json()
        return weather_info
    
def weatherContext(city):
    environmental_variables()
    weatherData = WeatherAPILoader(city=city, api_key=os.getenv("WEATHER_API_KEY"))
    return weatherData.load()

