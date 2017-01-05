import requests
from actions.handler import Action

class WeatherForecast(Action):
    def get_name(self):
        return "weather_forecast"

    def respond(self, settings, context):
        return "The weather will be sunny"
