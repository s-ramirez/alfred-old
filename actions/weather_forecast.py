import requests
from actions.handler import Action

class WeatherForecast(Action):
    def get_name(self):
        return "weather_forecast"

    def respond(self, settings, context):
        key = settings["api_keys"]["openweather"]
        location = Action.get_entity_type(context, "location")
        if(location is not None):
            return self.obtain_forecast(location["value"], key)

    def obtain_forecast(self, city, key):
        payload = { "APPID" : key, "q": city}
        r = requests.get('http://api.openweathermap.org/data/2.5/weather', params = payload)
        return self.build_response(r.json(), city)

    def build_response(self, response, location):
        report = response["weather"][0]
        if(response is not None):
            return "The weather is " + report["description"] + " in " + response["name"]
        return "Error performing request"
